# 03 — Parts, Labels, Device List

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md). Este es el grupo donde ya se
descubrió el error de fondo de la sesión: **confundir `partslist` con `label`**.

## Lección aprendida (léxico correcto)

| Si el usuario pide... | La acción correcta suele ser... | No... |
|---|---|---|
| "Exporta la lista de materiales/recambios **con la plantilla X**" (formato final con diseño, tipo Excel con macros) | `label` (`create_labels`, con `config_scheme`) | `partslist` — ignora `CONFIGSCHEME` en export sin avisar |
| "Exporta la lista de materiales en bruto" (datos planos, XML/CSV, para reimportar o integrar) | `partslist` (`export_parts_list`) | `label` — no es para intercambio de datos crudo |
| "Exporta/importa piezas del **sistema de gestión de piezas**" (parts DB global, no del proyecto) | `partsmanagementapi` (`partsmanagement_*`) | `partslist` — ese es a nivel de proyecto, no de la BD de piezas |

## `parts.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `export_parts_list` | `partslist /TYPE:EXPORT` | `export_file` (req), `project_name`, `format` | ⬜ | Probado en sesión previa bajo el servidor viejo (v1/v2, ya obsoleto) — **pendiente reverificar** con la tool unificada `eplan_export_parts_list`. Hallazgo a confirmar: valores válidos de `format` serían `XPalXmlExporter` (default) o `XPalCSVConverter`; **no existiría conversor Excel nativo** (`XLSX`/`Excel` fallaron con "interfaz no registrada"); el sistema no habría añadido la extensión automáticamente pese a la doc oficial; `CONFIGSCHEME` se habría ignorado en silencio en `TYPE:EXPORT` (solo aplicaría a `DELETESTOREDPROPERTIES`). |
| `import_parts_list` | `partslist /TYPE:IMPORT` | `import_file` (req), `project_name`, `format` | ⬜ | Mismos valores de `format` que export, probablemente. `FIELDASSIGNMENTSCHEME` y `MODE` (0/1/2) de la doc oficial **no están expuestos** en este wrapper — si se necesitan, usar `execute_raw_action`. |
| `select_part` | `XPamSelectPart` | — | ⬜ | 🚫 Abre diálogo interactivo de selección de pieza — no aplica bajo automatización desatendida/QuietMode real; solo tiene sentido con GUI visible. |
| `set_parts_data_source` | `XPartsSetDataSourceAction` | `data_source` (req) | ⬜ | 🚫 Cambia la fuente de datos de gestión de piezas de todo el sistema — confirmar antes, efecto global no solo de proyecto. |

## `labels.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `create_labels` | `label` | `destination_file` (req), `project_name`, `config_scheme`, `filter_scheme`, `sort_scheme`, `language`, `record_repeat`, `task_repeat`, `show_output`, `use_selection` | ⬜ | Probado en sesión previa bajo el servidor viejo (v1/v2) usando `config_scheme="Lista de recambios"` — **pendiente reverificar** con `eplan_create_labels`. Hallazgos a confirmar: (1) `destination_file` debería llevar la extensión que ya trae configurada el `CONFIGSCHEME` internamente (`.xlsx` dio error, `.xlsm` habría funcionado, confirmado por filesystem en `X:\Plantillas\v7.0\Recambios.xlsm`). (2) `language` parecería obligatorio de facto pese a figurar "optional" en la doc oficial — vacío lanzó `ArgumentException: strLanguage`; usar `es_ES` o el idioma real del proyecto. (3) `filter_scheme`/`sort_scheme` no habrían hecho falta si ya vienen definidos dentro del `config_scheme`. |

## `devicelist.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `export_device_list` | `devicelist /TYPE:EXPORT` | `export_file` (req), `project_name`, `format` (default `XDLXmlExporter`) | ⬜ | 🟢 A diferencia de `partslist`, aquí **el wrapper ya documenta el enum completo** en el propio docstring: `XDLXmlExporter`, `XDLTxtImporterExporter`, `XDLCsvImporterExporter`. No hace falta RAG para el formato — sí seguir el patrón de verificar si añade extensión sola (dudarlo, por precedente de `partslist`). |
| `import_device_list` | `devicelist /TYPE:IMPORT` | `import_file` (req), `project_name`, `format` | ⬜ | — |
| `delete_device_list` | `devicelist /TYPE:DELETE` | `project_name` | ⬜ | 🚫 Destructivo — confirmar antes. |

## `partsmanagement.py` (BD global de piezas, no el proyecto)

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `partsmanagement_export` | `partsmanagementapi /TYPE:EXPORT` | `export_file` (req), `format` (default `XPamExportXml`, alt. `IXPartsImportExportEdz` para `.edz`), `part_numbers`, `manufacturers`, `constructions`, `connection_patterns`, `accessory_lists`, `accessory_placements`, `filter_scheme` | ⬜ | 🟢 Formato documentado en el wrapper, no adivinar. Para "todas las piezas" usar `part_numbers=["*"]` o directamente `partsmanagement_export_all`. |
| `partsmanagement_import` | `partsmanagementapi /TYPE:IMPORT` | `import_file` (req), `format`, `mode` (0-3, ver tabla abajo), `additional_language`, `filter_scheme` | ⬜ | 🚫 Modifica la BD global de piezas — confirmar antes. `mode`: 0=solo añadir, 1=solo actualizar existentes, 2=actualizar+añadir, 3=reemplazar+añadir. |
| `partsmanagement_export_by_properties` | `partsmanagementapi /TYPE:<export_type>` | `export_type` (`EXPORTPARTS`\|`EXPORTMANUFACTURERS`\|`EXPORTCONSTRUCTIONS`\|`EXPORTCONNECTIONPATTERNS`\|`EXPORTACCESSORYLISTS`\|`EXPORTACCESSORYPLACEMENTS`), `export_file`, `properties` (dict `property_id: value`), `format` | ⬜ | Requiere conocer IDs de propiedad EPLAN (ej. `22024`=variante, `22007`=fabricante) — consultar RAG por nombre de propiedad antes de construir el dict, no adivinar el número. |
| `partsmanagement_export_all` | (wrapper de `partsmanagement_export` con `part_numbers=["*"]`) | `export_file`, `format` | ⬜ | — |

## Contexto que le falta a la LLM en este grupo

- **No hay forma de listar los `CONFIGSCHEME`/`FILTERSCHEME`/`SORTSCHEME` disponibles**
  desde el MCP. El único método que funcionó fue indirecto: buscar en el filesystem de
  master data (`X:\Plantillas`, `X:\Formularios`) un archivo cuyo nombre coincida con
  el del esquema, para inferir el formato/extensión de salida. Esto **no** confirma que
  el esquema exista realmente dentro de EPLAN (son sistemas distintos: uno es archivo
  de plantilla, otro es configuración registrada en el proyecto/sistema) — es una
  heurística, no una fuente de verdad. Ver propuesta en [TODO.md](TODO.md).
- **IDs de propiedad EPLAN** (`PROPERTYID`) para `partsmanagement_export_by_properties`
  — solo se pueden obtener fiablemente vía RAG (buscando el nombre de la property list,
  ej. `MDPartsDatabaseItemPropertyList`) o inspeccionando `parts_db_get_part` sobre una
  pieza conocida (ver `08-settings-scripted-addons-scripts-ribbon.md`).
