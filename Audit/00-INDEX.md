# Audit del MCP `eplan` — Índice

Objetivo: probar **una por una** las 149 acciones que expone el servidor local `eplan`
(ver `llm.md` en la raíz del repo), documentar el uso real (no el que dice el docstring
de Python, sino el que exige EPLAN en la práctica), y anotar qué contexto le falta a la
LLM para usarlas sin tener que preguntar o adivinar.


## Leyenda de estado

| Símbolo | Significado |
|---|---|
| ⬜ | No probada todavía |
| 🟡 | Probada, funciona pero con matices/gotchas importantes |
| ✅ | Probada, funciona tal como se documenta aquí |
| ❌ | Probada, falla o bloqueada (ver nota) |
| 🚫 | No probable de forma segura sin más contexto (destructiva, necesita GUI, etc.) |

## Metodología por acción

1. Anotar el nombre de la acción EPLAN real (`Action:` en el docstring) y sus
   parámetros según la doc oficial de `eplan.help` (vía RAG:
   `POST https://rag2026.covaga.xyz/search`), **no inventar valores**.
2. Ejecutar con el proyecto de prueba abierto.
3. Si `success: false` sin mensaje útil — ver `TODO.md`, es una limitación conocida
   del wrapper (traga excepciones). Intentar diagnosticar por tamaño/contenido del
   archivo resultante o repitiendo con `execute_raw_action` / `execute_custom_script`.
4. Registrar en la tabla: parámetros reales usados, resultado, y cualquier "esquema"
   (CONFIGSCHEME/FILTERSCHEME/SORTSCHEME/plantilla) que la acción haya necesitado y
   cómo se descubrió (RAG, filesystem de master data, prueba/error).

## Archivos

| Archivo | Módulos Python | Acciones EPLAN cubiertas |
|---|---|---|
| [01-project-workspace-backup.md](01-project-workspace-backup.md) | `project.py`, `workspace.py`, `backup.py` | ProjectOpen, projectmanagement, backup, restore, workspace... |
| [02-export-import.md](02-export-import.md) | `export_.py`, `import_.py` | export (PDF/DXF/DWG/gráficos/PXF), export3d, import, import3d |
| [03-parts-labels-devicelist.md](03-parts-labels-devicelist.md) | `parts.py`, `partsmanagement.py`, `labels.py`, `devicelist.py` | partslist, partsmanagementapi, label, devicelist |
| [04-data-exchange-plc-production.md](04-data-exchange-plc-production.md) | `data_exchange.py`, `plc.py`, `production.py` | XM*Export*, masterdata, subprojects, plcservice, NC/wiring |
| [05-reports-macros-cabinet.md](05-reports-macros-cabinet.md) | `reports.py`, `macros.py`, `cabinet.py` | reports, generatemacros, Topology, segment filling |
| [06-navigation-search-properties.md](06-navigation-search-properties.md) | `navigation.py`, `search.py`, `properties.py` | edit, selectionset, search, XEs*Property* |
| [07-renumber-layers-translate-print.md](07-renumber-layers-translate-print.md) | `renumber.py`, `layers.py`, `translate.py`, `print_.py` | renumber, changelayer, graphicallayertable, translate, print |
| [08-settings-scripted-addons-scripts-ribbon.md](08-settings-scripted-addons-scripts-ribbon.md) | `settings.py`, `scripted.py`, `addons.py`, `scripts.py`, `ribbon.py` | XSettings*, parts_db_*, settings_get/set_*, pathmap_*, RegisterScript, ribbon |
| [TODO.md](TODO.md) | — | Gaps de la plataforma: visibilidad de errores, "loader" visual, descubrimiento de esquemas |

## Estado de este audit: partimos de 0

Todas las acciones están marcadas ⬜ (no probadas), incluidas `export_parts_list` y
`create_labels`, que se habían probado en una sesión previa **bajo el servidor MCP
viejo (split v1/v2, ya obsoleto y no presente en `main`)**. Esos resultados quedan
como hipótesis a reverificar, no como hechos confirmados — ver notas en
`03-parts-labels-devicelist.md`. Ningún hallazgo de esta sesión anterior se da por
válido hasta repetirlo con la tool unificada (`eplan_<nombre>`) actual.

## Limitación estructural encontrada

`eplan_connection.py:336` ejecuta las acciones vía
`CommandLineInterpreter.Execute(action_name, acc)`, que **atrapa las excepciones de
EPLAN internamente y solo devuelve `bool`**. Por eso, cuando un parámetro es inválido
(ej. `FORMAT:XLSX`, `LANGUAGE` vacío), el resultado es `{"success": false, "parameters": {...}}`
**sin ningún mensaje** — el texto real (el que ve el usuario en la ventana de EPLAN)
nunca llega al script C# que envuelve la llamada. Detalle técnico y propuesta de fix
en `TODO.md`.
