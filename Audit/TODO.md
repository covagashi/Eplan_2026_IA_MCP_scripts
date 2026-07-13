# TODO — Gaps de la plataforma MCP `eplan`

No son tareas para la LLM dentro de una conversación — son mejoras al **servidor MCP
en sí** (`eplan-p8-mcp-server/`) que reducirían la necesidad de adivinar, preguntar al
usuario, o fallar en silencio. Cada una nace de un problema real observado en esta
sesión, no es especulación.

---


## 1. Los errores reales de EPLAN nunca llegan a la LLM

### Causa raíz (confirmada leyendo el código, no especulada)

`eplan_connection.py:336`, dentro de `execute_action()`:

```csharp
var cli = new CommandLineInterpreter();
bool success = cli.Execute("{action_name}", acc);
results["success"] = success;
```

`CommandLineInterpreter.Execute()` **atrapa internamente** las excepciones que lanza
la acción EPLAN subyacente (`ArgumentException`, `BaseException`, etc. — las mismas
que sí se le muestran al usuario humano en un MessageBox dentro de la GUI de EPLAN) y
simplemente devuelve `false`. El `catch (Exception ex)` que envuelve todo el script en
`eplan_connection.py:357-361` **nunca se dispara** para estos casos, porque no hay
excepción que propague — el propio `Execute()` la absorbe.

Resultado observado dos veces en esta sesión: `{"success": false, "parameters": {...}}`
sin ningún campo `message`/`error`, mientras que el usuario, mirando la pantalla de
EPLAN, veía el texto completo del error (ej. *"El idioma no es válido. Nombre del
parámetro: strLanguage"*). La LLM literalmente no tiene acceso a esa información salvo
que el usuario la copie y pegue a mano — que es exactamente lo que pasó.

**Matiz adicional, confirmado 2026-07-13 con `restore_masterdata`**: `success:false`
tampoco es fiable como señal de "la acción no hizo nada". Probado con `destination_path`
igual a la carpeta que contenía el propio `archive_name` (comportamiento de overwrite
esperado, no un bug — aclarado por Christian): la llamada devolvió `{"success": false}`
sin mensaje, pero el overwrite sobre `destination_path` sí ocurrió, afectando archivos
hermanos no relacionados que estaban en esa carpeta. Un fix de este punto (1) idealmente
capturaría también ese desfase entre el flag `success` y lo que realmente pasó en
disco, no solo el mensaje de la excepción cuando la hay. Ver
`Audit/01-project-workspace-backup.md`, fila `restore_masterdata`.

### Opciones de fix (de menor a mayor esfuerzo)

1. **Reemplazar `CommandLineInterpreter.Execute` por la clase `Action` directa**
   (`Eplan.EplApi.ActionManagement.Action`), que si lanza excepciones de verdad — es
   lo que usé manualmente en esta sesión vía `execute_custom_script` para intentar
   diagnosticar `create_labels`. Cambiar la generación de script en
   `eplan_connection.py` para usar:
   ```csharp
   var action = new Eplan.EplApi.ActionManagement.Action("{action_name}");
   bool success = action.Execute(acc);
   ```
   dentro del mismo `try/catch` ya existente. Riesgo: verificar que el comportamiento
   bajo `QuietModeStep` sea idéntico (algunas acciones podrían depender de
   particularidades de `CommandLineInterpreter`).
2. **Enganchar el sistema de mensajes de EPLAN** (`Eplan.EplApi.Base.MessageManager`
   o equivalente) antes de `cli.Execute(...)` y volcar su contenido después,
   independientemente de si hubo excepción o no. Esto capturaría también avisos que
   no son excepciones (warnings). Requiere investigar la API exacta de mensajes de
   EPLAN vía RAG antes de implementar — no asumir el nombre de la clase.
3. Combinar 1+2: usar `Action.Execute` para excepciones duras, y el message log para
   los `success:false` "silenciosos" que no lanzan nada pero tampoco hacen lo pedido.

---

## 2. El usuario no ve que la LLM está operando EPLAN ("loader" visual)

Todas las acciones corren bajo `QuietModeStep(QuietModes.ShowNoDialogs)` — por diseño,
para que no aparezcan diálogos que bloqueen la automatización. Efecto secundario: si
el usuario tiene la GUI de EPLAN abierta mientras la LLM opera, **no hay ninguna señal
visual** de qué se está ejecutando, cuándo empezó, ni si terminó. Además, cuando algo
sí requiere interacción humana (ej. el timeout de 30s que sufrimos con `FORMAT:Excel`
vía COM), el usuario no tiene forma de saber que hay un diálogo esperando en algún
lugar sin ir a buscarlo manualmente.

### Propuesta

Antes de `cli.Execute(...)` en el script C# generado, escribir un mensaje breve en un
lugar visible de la GUI que no requiera interacción — candidato principal: la barra de
estado de EPLAN (`Eplan.EplApi.ApplicationFramework` — investigar el nombre exacto de
la clase de status bar vía RAG antes de implementar, no asumir). Ejemplo de mensaje:

```
🤖 Claude ejecutando: partslist /TYPE:EXPORT ...
```

y limpiarlo (o mostrar "✓ hecho" / "✗ falló") en el `finally` del mismo script. Esto:

- Da visibilidad en tiempo real sin reintroducir diálogos bloqueantes.
- Si algo se cuelga (como el caso de `execute_custom_script` con Excel), el usuario ve
  el último mensaje y sabe qué buscar/cerrar manualmente en vez de ver la GUI "muda".

### Complemento: log persistente

Además del indicador visual efímero, escribir cada acción ejecutada (nombre, params,
resultado, timestamp) a un archivo de log append-only
(`eplan-p8-mcp-server/mcp_server/logs/actions.log` o similar). Esto es independiente
del fix del punto 1 — incluso si nunca se resuelve la captura de excepciones, un log
de "qué se intentó y cuándo" ayuda a correlacionar con lo que el usuario vio en
pantalla, y da trazabilidad para este mismo tipo de audit sin depender de que la LLM
recuerde todo dentro de una única conversación.

---

## 3. No hay forma de descubrir "esquemas" sin adivinar o preguntar

Repetido en casi todos los archivos del audit (`02`, `03`, `04`, `05`, `07`, `08`):
`CONFIGSCHEME`, `FILTERSCHEME`, `SORTSCHEME`, `export_scheme`, `import_scheme`,
`scheme` (project_management), `templates` (reports), `layer_name`, `setting_path`
— todos son catálogos que viven dentro de la configuración de EPLAN/proyecto y que
ninguna tool actual permite enumerar.

**Ya existe un precedente de cómo resolver esto bien dentro del propio código**:
`parts_db_list_product_groups()` en `scripted.py` usa `Enum.GetNames(typeof(...))`
para devolver un catálogo real leído de la API, no adivinado. Es el patrón a replicar.



