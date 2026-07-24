# 04 — Data Exchange, PLC, Producción

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md).

## `data_exchange.py`

Casi todas estas acciones comparten firma (`destination`, `config_scheme`,
`language`, `complete_project`, `execution_mode`, `immediate_import`) y todas
dependen de un `CONFIGSCHEME` que determina el formato de salida (TXT/XLS/XLSX/XML)
— **mismo patrón de riesgo que `label`**: si no se pasa `config_scheme`, la doc dice
literalmente *"a dialog asks for it"*, lo cual bajo QuietMode probablemente cuelga o
falla silenciosamente en vez de mostrar el diálogo. **Nunca invocar estas sin
`config_scheme` explícito.**

| Tool | Acción EPLAN | Notas específicas | Estado |
|---|---|---|---|
| `export_connections` | `XMExportConnectionsAction` | Docstring del propio wrapper avisa: **obsoleta**, preferir `dc_export`. `execution_mode`: 0=solo exportar, 1=exportar y editar, 2=editar y devolver. | ⬜ |
| `export_functions` | `XMExportFunctionAction` | Igual, preferir `dc_export`. | ⬜ |
| `export_pages` | `XMExportPagesAction` | Igual, preferir `dc_export`. | ⬜ |
| `dc_import` | `XMActionDCImport` | Importa un `.edc` (data configuration). | ⬜ 🚫 Modifica propiedades de funciones — confirmar antes. |
| `dc_export` | `XMActionDCCommonExport` | **La acción recomendada** para exportar conexiones/funciones/páginas/etc. — usar esta en vez de las 3 anteriores. Probada 2026-07-24 en batch real de 467 proyectos (`1.- ROBOTICA`, `config_scheme=Test`, `complete_project=1`, `execution_mode=2`, `immediate_import=1`): **467/467 success, 0 errores**, corrido como script único en EPLAN (loop en C# vía `execute_custom_script`, no 467 llamadas MCP sueltas). Hallazgo clave: como todo el wrapper corre bajo QuietMode (`_base.py`), `execution_mode=2` ("Edit and return") **no pausa para edición manual** — el diálogo/editor se suprime y con `immediate_import=1` el dato se reimporta esencialmente sin cambios (roundtrip). Si se necesita edición humana real antes de reimportar, este wrapper no lo permite; usar `execution_mode=0` y manejar edición/reimport aparte. Docstring del wrapper actualizado con este detalle. | 🟡 |
| `export_dc_article_data` | `XMExportDCArticleDataAction` | — | ⬜ |
| `import_dc_article_data` | `XMImportDCArticleDataAction` | Sin `config_scheme` en la firma — probablemente el formato lo define el archivo de origen. | ⬜ 🚫 Confirmar antes. |
| `export_location_boxes` | `XMExportLocationBoxesAction` | Obsoleta según docstring, preferir `dc_export`. | ⬜ |
| `export_potential_definitions` | `XMExportPotentialDefsAction` | Obsoleta, preferir `dc_export`. | ⬜ |
| `export_pipeline_definitions` | `XMExportPipeLineDefsAction` | — | ⬜ |
| `delete_representation_type` | `XMDeleteReprTypeAction` | Sin más parámetros que `project_name` — alcance ambiguo (¿cuál tipo de representación borra?). Consultar RAG antes del primer uso. | ⬜ |
| `correct_connections` | `EsCorrectConnections` | Sin parámetros — fusiona propiedades gráficas de puntos de definición de conexión. | ⬜ 🚫 Modifica geometría del proyecto — confirmar antes. |
| `remove_unnecessary_ndps` | `XCMRemoveUnnecessaryNDPsAction` | Sin parámetros. | ⬜ 🚫 Destructivo sobre puntos de definición de red — confirmar. |
| `unite_net_definition_points` | `XCMUniteNetDefinitionPointsAction` | Sin parámetros. | ⬜ 🚫 Igual, confirmar. |
| `export_subproject` | `subprojects /TYPE:FILEOFF` | ⚠️ Requiere proyecto abierto en **modo exclusivo**, y tras ejecutarla "el objeto del proyecto origen queda inválido" (doc del propio wrapper) — implica que hay que reabrir el proyecto después. | ⬜ 🚫 Alto impacto, confirmar. |
| `import_subproject` | `subprojects /TYPE:STORE` | Igual, requiere modo exclusivo. | ⬜ 🚫 Confirmar. |
| `masterdata_operation` | `masterdata` | `operation_type` sin enum documentado en el wrapper — **consultar RAG antes de usar**, no adivinar valores de `TYPE`. | ⬜ |

## `plc.py`

| Tool | Acción EPLAN | Parámetros clave | Estado | Notas |
|---|---|---|---|---|
| `plc_export` | `plcservice /TYPE:BUSDATAEXPORT` | `destination_file` (req), `converter_id` (req — ej. `PlcDcXMLExchangerSiemens`, `PlcDcAMLExchangerGeneral`, `PlcDcXMLExchangerSchneider`), `configuration_project`, `language`, `overwrite`, `format` (solo para converters con múltiples formatos, ej. `"AutomationML AR APC V1.4.0"`) | ⬜ | El `converter_id` correcto depende del fabricante del PLC del proyecto — preguntar al usuario o inspeccionar el proyecto si no es evidente, no asumir Siemens por defecto. |
| `plc_import` | `plcservice /TYPE:BUSDATAIMPORT` | `source_file` (req), `converter_id` (req), `project_name`, `language`, `import_match` (0=por ID interno, 1=por nombre con posible diálogo de comparación, 2=no emparejar, crea todo nuevo) | ⬜ | 🚫 `import_match=1` puede disparar un diálogo de comparación — bajo QuietMode esto es un riesgo de cuelgue (mismo patrón que el timeout que tuvimos con `FORMAT:Excel` vía COM). Preferir `0` o `2` en automatización desatendida. |

## `production.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `export_nc_data` | `ExportNCData` | `export_file` (req), `project_name` | ⬜ | Datos de mecanizado CNC para máquinas — sin parámetros de formato, revisar si el `export_file` determina el tipo por extensión. |
| `export_production_wiring` | `ExportProductionWiring` | `export_file` (req), `project_name` | ⬜ | — |

## Riesgo transversal de este grupo: diálogos bajo QuietMode

Varias acciones aquí mencionan explícitamente en su propia documentación que, si
falta un parámetro (`config_scheme` en `dc_export`, `import_match=1` en `plc_import`),
EPLAN **muestra un diálogo interactivo**. Ya se observó en esta sesión que un intento
de exportación que necesitaba interacción (formato Excel vía COM) **colgó
`execute_custom_script` durante 30s hasta timeout**, sin bloquear el resto de la
conexión (EPLAN seguía respondiendo a otras acciones — sugiere que quedó un diálogo
modal abierto esperando input humano). Antes de invocar cualquier acción de este
archivo sin todos los parámetros que evitan el diálogo, asumir que puede colgar la
llamada 30s y no repetir en bucle — reportar al usuario que puede haber quedado un
diálogo abierto en la GUI de EPLAN esperando que lo cierren manualmente.
