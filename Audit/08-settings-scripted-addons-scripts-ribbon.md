# 08 — Settings, Scripted APIs, Add-ons, Scripts, Ribbon

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md).

## `settings.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `export_settings` | `XSettingsExport` | `xml_file` (req), `node` (ej. `"USER"`, `"STATION"`, `"COMPANY"`, `"USER.DIALOGSETTINGS"`), `project` | ⬜ | 🟢 El wrapper documenta ejemplos reales de `node` en su propio docstring — no adivinar, usar esos como plantilla y ajustar el sufijo. |
| `import_settings` | `XSettingsImport` | `xml_file`, `node`, `project` | ⬜ | 🚫 Si `xml_file` se deja vacío, la doc dice que **aparece un diálogo de selección de archivo** — bajo QuietMode esto es exactamente el patrón que ya causó un timeout de 30s (ver `04-...md`). **Nunca omitir `xml_file`.** |
| `set_setting` | `XAfActionSetting` | `name` (req, ej. `"USER.MacrosLog.Pxf.writeDebugInfo"`), `value` (req), `index` | 🚫 | Modifica configuración global de usuario/estación — confirmar antes. |
| `set_project_setting` | `XAfActionSettingProject` | `name` (req), `value` (req), `project`, `index` | 🚫 | Modifica configuración del proyecto — confirmar antes. |

## `scripted.py` (APIs avanzadas — se ejecutan como C# vía `execute_custom_script` internamente)

Este módulo no envuelve acciones EPLAN tradicionales (`Action:` + `TYPE:`), sino que
genera y ejecuta scripts C# directos contra `Eplan.EplApi.MasterData`/`Base` — son
más flexibles pero también más opacos si algo falla (mismo problema de captura de
errores que el resto, ver `TODO.md`).

| Tool | Qué hace | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `parts_db_query` | Query directa a la BD de piezas vía `MDPartsManagement` | `filter_property`, `filter_value`, `return_properties` (default: PartNr, Description1, Manufacturer, ProductGroup, ProductSubGroup), `limit` (default 100) | ⬜ | Read-only, buen candidato de test temprano. `filter_property` debe ser un nombre de propiedad C# válido de `MDPartsDatabaseItem` — si no existe, probablemente el LINQ `.Where` falla silenciosamente o lanza. |
| `parts_db_count` | Cuenta piezas con filtro opcional | `filter_property`, `filter_value` | ⬜ | Read-only, seguro. |
| `parts_db_get_part` | Detalle de una pieza por número | `part_number` (req) | ⬜ | Read-only. Devuelve `found: false` si no existe (no es un error) — no confundir con fallo real. |
| `parts_db_update` | Actualiza una propiedad de una pieza | `part_number` (req), `property_name` (req), `property_value` (req) | 🚫 | Escribe en la BD global de piezas — confirmar antes. |
| `parts_db_list_product_groups` | Lista los enums `ProductGroup`/`ProductSubGroup`/`ProductTopGroup` completos | — | ⬜ | 🟢 **Esta es la respuesta al problema de "no sé qué grupos de producto existen"** — es la única tool de todo el MCP que devuelve un catálogo cerrado real (viene de un `Enum.GetNames` de la API, no adivinado). Usar antes de filtrar por `ProductGroup` en cualquier otra acción de piezas. |
| `settings_get_string` / `settings_set_string` | Get/set typed de un setting string | `setting_path` (ej. `"USER.TrDMProject.UserData.Longname"`), `value` (solo set), `index` | ⬜ | `setting_path` es un namespace jerárquico propio de EPLAN — mismo problema de descubrimiento que los `*scheme`; usar `export_settings` primero para ver el árbol real como XML si no se conoce la ruta exacta. |
| `settings_get_bool` / `settings_set_bool` | Igual, tipo bool | igual | ⬜ | — |
| `settings_get_int` / `settings_set_int` | Igual, tipo int | igual | ⬜ | — |
| `settings_get_double` / `settings_set_double` | Igual, tipo double | igual | ⬜ | — |
| `pathmap_substitute` | Sustituye variables de ruta EPLAN (`$(MD_FORMS)`, etc.) en un string | `path_with_variables` (req) | ⬜ | — |
| `pathmap_get_common_paths` | Devuelve todas las variables de ruta comunes y su valor actual | — | ⬜ | Probado en sesión previa (bajo servidor viejo) sin incidentes — devolvió `$(PROJECTPATH)`, `$(MD_FORMS)`, `$(MD_PARTS)`, etc. Pendiente reverificar con la tool unificada, pero de bajo riesgo (read-only). Es la vía recomendada para resolver rutas de master data en vez de hardcodear `X:\...`. |
| `execute_custom_script` | Ejecuta C# arbitrario contra `Eplan.EplApi.*` | `script_code` (req, debe escribir el resultado a `{{RESULT_PATH}}`) | ⬜ | ⚠️ **Riesgo de cuelgue confirmado** — en esta sesión, un intento de automatizar una exportación que internamente dependía de interacción (Excel vía COM) colgó esta tool durante los 30s completos de timeout. Es el escape hatch de último recurso; evitar si hay una acción wrapeada equivalente. |

## `addons.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `load_api_module` | `EplApiModuleAction` | `module_path` (req, DLL de add-in) | 🚫 | Carga y registra código externo en el proceso de EPLAN — alto riesgo, confirmar siempre. |
| `register_addon` | `XSettingsRegisterAction` | `addon_path` o `install_file` (uno de los dos) | 🚫 | Igual, confirmar antes. |
| `unregister_addon` | `XSettingsUnregisterAction` | `addon_path` o `install_file` | 🚫 | Igual, confirmar antes. |
| `execute_raw_action` | (cualquiera) | `action_string` (req, string completo tipo `'ActionName /PARAM:value'`) | ⬜ | Escape hatch general — usado ya en sesión previa para pasar `CONFIGSCHEME` a `partslist` sin soporte del wrapper específico. Útil, pero hereda el mismo problema de captura de errores silenciosa que toda acción vía `execute_action`. |

## `scripts.py`

⚠️ Estas tres son **infraestructura interna** — `eplan_connection.py` las usa a su vez
para envolver TODAS las demás acciones bajo QuietMode (ver `TODO.md`). Llamarlas
manualmente es de bajo nivel.

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `register_script` | `RegisterScript` | `script_file` (req) | ⬜ | — |
| `unregister_script` | `UnregisterScript` | `script_file` (req) | ⬜ | — |
| `execute_script` | `ExecuteScript` | `script_file` (req) | ⬜ | — |

## `ribbon.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `export_ribbon_bar` | `MfExportRibbonBarAction` | `export_file` (req) | ⬜ | Read-only, bajo riesgo. |
| `import_ribbon_bar` | `MfImportRibbonBarAction` | `import_file` (req) | 🚫 | Cambia la personalización de la barra de cintas de la GUI — confirmar antes (efecto visible/molesto para el usuario humano si comparte la misma sesión de EPLAN). |

## Contexto que le falta a la LLM en este grupo

- **`parts_db_list_product_groups` es el único caso en todo el audit de una tool que
  resuelve completamente el problema de "catálogo desconocido"** — devuelve el enum
  real vía reflexión C#, no requiere RAG ni heurísticas de filesystem. Es el patrón a
  replicar: cuando se proponga una tool nueva de descubrimiento de schemes (ver
  `TODO.md`), este es el modelo a seguir (leer el enum/registro real de EPLAN, no
  adivinar).
- `settings_get/set_*` dependen de conocer el `setting_path` exacto — no hay una tool
  de "listar todos los settings", solo `export_settings` a XML como fallback indirecto
  (hay que exportar y leer el archivo, no es instantáneo).
