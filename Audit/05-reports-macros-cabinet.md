# 05 — Reports/Evaluaciones, Macros, Cabinet/3D

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md).

## `reports.py`

Las 5 acciones de este módulo son **un único action name EPLAN (`reports`)**
diferenciado por `TYPE:`.

| Tool | `TYPE` interno | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `update_reports` | `PROJECT` o `PAGES` (auto-detectado según si se pasan páginas) | `project_name`, `page_name`, `page_names`, `page_identifiers`, `use_page_filter`, `page_filter_name` | ⬜ | Esta acción **actualiza** páginas de reporte/evaluación ya existentes en el proyecto — no crea una lista nueva desde cero con una plantilla (eso es `label`, ver `03-...md`). Confundir ambas es el mismo tipo de error que ya cometimos con `partslist` vs `label`. |
| `update_model_view_pages` | `UPDATEMODELVIEWPAGES` | igual que arriba | ⬜ | — |
| `create_model_views` | `CREATEMODELVIEWS` | `project_name`, `templates` (lista), `replace_existing` | ⬜ | `templates` — nombres de plantilla, mismo problema de descubrimiento que otros `*scheme`. |
| `create_copper_unfolds` | `CREATECOPPERUNFOLDS` | igual que `create_model_views` | ⬜ | — |
| `create_drilling_views` | `CREATEDRILLINGVIEWS` | igual que `create_model_views` | ⬜ | — |

## `macros.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `generate_macros` | `generatemacros` | `project_name`, `destination_path`, `scheme` | ⬜ | `scheme` sin enum — RAG antes de adivinar. |
| `prepare_macros` | `preparemacros` | `project_name` | ⬜ | — |
| `update_macros` | `XGedUpdateMacroAction` | `project_path`, `scheme_name` | ⬜ | 🟢 Doc del propio wrapper dice explícitamente: si se omite `scheme_name`, usa **"el último esquema usado"** — mismo comportamiento por defecto que vimos en `label`/`partslist`. Y si se omite `project_path`, usa el objeto seleccionado en el GED (no el proyecto abierto necesariamente) — cuidado con la diferencia. |

## `cabinet.py` (3D / Armario)

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `calculate_cabinet_weight` | `XCabCalculateEnclosureTotalWeightAction` | `project_name` | ⬜ | Read-only en apariencia (calcula, no debería modificar geometría) — buen candidato para probar primero sin riesgo. |
| `update_segments_filling` | `UpdateSegmentsFilling` | `project_name` | ⬜ | Calcula y **fija** valores de llenado de segmento — modifica datos del proyecto. |
| `topology_operation` | `Topology` | `operation_type` (req, sin enum documentado), `project_name` | ⬜ | **Consultar RAG por el nombre exacto de la acción `Topology` antes de usar** — `operation_type` totalmente opaco en el wrapper actual. |
| `import_preplanning_data` | `ImportPrePlanningData` | `import_file` (req), `project_name` | ⬜ | 🚫 Importa datos de preplanificación — confirmar antes. |
| `export_segments_template` | `ExportSegmentsTemplate` | `export_file` (req), `project_name` | ⬜ | — |
| `import_segments_template` | `ImportSegmentsTemplate` | `import_file` (req), `project_name` | ⬜ | 🚫 Confirmar antes (modifica plantillas de segmento del proyecto). |

## Contexto que le falta a la LLM en este grupo

- `topology_operation.operation_type` es el más opaco de todo este archivo: cero pistas
  en el wrapper sobre los valores válidos de `TYPE` para la acción `Topology`. Es
  prioridad alta para consulta RAG antes del primer test real.
- Igual que en otros grupos, `templates` en `create_model_views`/`create_copper_unfolds`/
  `create_drilling_views` no se puede enumerar desde el MCP — earch por nombre de
  archivo en master data (patrón que funcionó con `Recambios.xlsm`) es el único
  fallback conocido hasta que exista una tool de descubrimiento (ver `TODO.md`).
