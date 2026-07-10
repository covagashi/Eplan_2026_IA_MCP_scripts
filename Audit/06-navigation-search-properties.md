# 06 — Navegación, Búsqueda, Propiedades

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md). Este grupo es mayormente
**read-only / de bajo riesgo** — buen punto de partida para el testing sistemático.

## `navigation.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `edit_open_page` | `edit` | `page_name` (req), `project_name`, `x`, `y` | ⬜ | Bajo QuietMode remoto, "abrir página" puede no tener efecto visible (no hay GUI) — verificar qué devuelve realmente. |
| `edit_goto_device` | `edit` | `device_name` (req), `project_name` | ⬜ | — |
| `edit_open_layout_space` | `edit` | `installation_space` (req), `project_name` | ⬜ | — |
| `close_pages` | `XGedClosePage` | — | ⬜ | 🚫 Cierra páginas seleccionadas — confirmar si hay cambios sin guardar. |
| `redraw_ged` | `gedRedraw` | — | ⬜ | 🟢 El propio wrapper ya documenta que **devuelve `FALSE` bajo QuietMode** (que este servidor siempre fuerza) — al probarlo, un `success:false` aquí es el comportamiento esperado y no un bug. |
| `get_selected_pages` | `selectionset /TYPE:PAGES` | — | ⬜ | Devuelve `PAGES` separado por `;`. Útil para poblar `page_identifiers` de otras acciones (export_pdf_pages, etc.) — probarlo primero en flujos que requieran `SELn`. |
| `preview_page` | `XSDPreviewAction` | `page_name`, `project_name`, `macro_name`, `open` (default `True`) | ⬜ | Si se omiten `page_name` y `macro_name`, muestra **todas** las páginas del proyecto — cuidado con proyectos grandes. |
| `navigate_to_eec` | `navigateToEEC` | `object_id` (req) | ⬜ | Requiere conocer el `EECOBJECTID` de antemano — no hay forma obvia de obtenerlo desde otras tools de este MCP; posible gap. |

## `search.py`

Todas comparten `Action: search`, diferenciadas por `TYPE`. Ninguna tiene parámetros
opacos tipo `scheme` sin documentar — **bajo riesgo, buenos candidatos para probar ya**.

| Tool | `TYPE` interno | Parámetros distintivos | Estado |
|---|---|---|---|
| `search_devices` | `DEVICETAG` | `search_item` (req), `case_sensitive`, `whole_text` | ⬜ |
| `search_text` | `TEXTS` | + `logic_pages`, `graphic_pages`, `evaluation_pages`, `not_placed_functions`, `filter_scheme` | ⬜ |
| `search_all_properties` | `ALLPROPERTIES` | `search_item`, `case_sensitive` | ⬜ |
| `search_page_data` | `PAGEDATA` | igual que `search_text` | ⬜ |
| `search_project_data` | `PROJECTDATA` | `search_item`, `case_sensitive`, `whole_text` | ⬜ |

`filter_scheme` en `search_text`/`search_page_data` es opcional y, si se omite,
probablemente no filtra — bajo riesgo, no bloquea el uso básico de estas acciones.

## `properties.py`

⚠️ **Ojo con el alcance implícito** — varias de estas NO toman `project_name`/`page_name`
como parámetro; operan sobre "lo actualmente seleccionado":

| Tool | Acción EPLAN | Alcance real | Parámetros | Estado | Notas |
|---|---|---|---|---|---|---|
| `get_project_property` | `XEsGetProjectPropertyAction` | Proyecto **actual** (no hay `PROJECTNAME`) | `property_id` (req), `property_index` | ⬜ | `property_id` viene de `Eplan.EplApi.DataModel.Properties` — consultar RAG por el nombre de la propiedad deseada antes de adivinar el número/nombre. |
| `set_project_property` | `XEsSetProjectPropertyAction` | Proyecto actual | `property_id` (req), `value` (req), `property_index` | ⬜ | 🚫 Modifica el proyecto actual — confirmar antes. |
| `get_page_property` | `XEsGetPagePropertyAction` | **Primera página seleccionada** (no hay `PAGENAME`) | `property_id` (req), `property_index` | ⬜ | Requiere que haya una página seleccionada de antemano — combinar con `get_selected_pages`/`edit_open_page` primero. |
| `set_page_property` | `XEsSetPagePropertyAction` | Páginas **seleccionadas** | `property_id` (req), `value` (req), `property_index` | ⬜ | 🚫 Confirmar antes. |
| `get_property` | `XEsGetPropertyAction` | Objetos **seleccionados** | `property_id` o `property_ident_name` (uno de los dos req), `property_index` | ⬜ | `property_ident_name` es la vía para propiedades definidas por el usuario (no numéricas). |
| `set_property` | `XEsSetPropertyAction` | Objetos seleccionados | `value` (req), `property_id` o `property_ident_name`, `property_index` | ⬜ | 🚫 Confirmar antes. |
| `export_user_properties` | `XEsUserPropertiesExportAction` | Proyecto | `export_file` (req), `project_name` | ⬜ | — |
| `import_user_properties` | `XEsUserPropertiesImportAction` | Proyecto | `import_file` (req), `project_name` | ⬜ | 🚫 Confirmar antes. |

## Contexto que le falta a la LLM en este grupo

- **IDs/nombres de propiedad EPLAN** (`PropertyId`) — es un catálogo enorme
  (`Eplan.EplApi.DataModel.Properties`, cientos de constantes tipo `FUNC_ARTICLE_SPARE`,
  `PROJ_...`, etc.). Consultar el RAG por el nombre semántico de la propiedad
  (ej. "número de artículo", "fabricante") antes de adivinar el ID — ya se vio en la
  sesión previa que el RAG sí indexa estas property lists (`MDPartsDatabaseItemPropertyList`,
  `ConnectionPropertyList`, etc.).
- **`navigate_to_eec(object_id)`** — no hay ninguna tool en este MCP que devuelva un
  `EECOBJECTID` para poder navegar; posible gap real de la plataforma, no solo de
  contexto de la LLM.
- Las acciones "sin `PROJECTNAME`/`PAGENAME`" (`get_page_property`, `get_property`,
  `set_property`) dependen de un **estado de selección previo** en la GUI de EPLAN —
  bajo una sesión 100% remota/automatizada esto es frágil: si nadie ha seleccionado
  nada, probablemente fallan o devuelven vacío. Antes de reportar un fallo como "bug",
  verificar si el problema es simplemente que no había selección activa.
