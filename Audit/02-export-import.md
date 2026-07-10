# 02 — Export / Import (PDF, DXF, DWG, gráficos, PXF, 3D)

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md). Todas las acciones de este grupo
usan `Action: export` / `Action: import` / `Action: export3d` / `Action: import3d`
(un único action name de EPLAN, diferenciado internamente por `TYPE:`).

## `export_.py`

| Tool | `TYPE` interno | Parámetros clave | Estado | Notas |
|---|---|---|---|---|
| `export_pdf_project` | `PDFPROJECTSCHEME` | `export_file` (req), `export_scheme`, `black_white` (0-3), `language`, `use_zoom`, `zoom_level`, `use_simple_link`, `fast_web_view`, `read_only`, `use_print_margins`, `export_model` | ⬜ | `export_scheme` = esquema de exportación PDF — mismo problema de descubrimiento que `CONFIGSCHEME`. Sin `export_scheme` probablemente usa "el último usado" (patrón visto en `label`/`partslist`). |
| `export_pdf_pages` | `PDFPAGESSCHEME` | `export_file` (req), `page_names` o `page_identifiers`, resto igual que arriba | ⬜ | `page_identifiers` requiere `StorableObject.ToStringIdentifier()` — formato interno, probablemente solo se obtiene con `get_selected_pages` primero. |
| `export_dxf_project` | `DXFPROJECT` | `destination_path` (req), `export_scheme`, `language`, `target` (`Disk`\|`FromSettings`) | ⬜ | — |
| `export_dxf_pages` | `DXFPAGE` | `destination_path`, `page_name`/`page_names`, `export_scheme`, `language`, `target` | ⬜ | Doc dice `destination_path` se ignora si se usa `PAGENAMEn` con scheme — verificar en la práctica. |
| `export_dwg_project` | `DWGPROJECT` | igual que DXF project | ⬜ | — |
| `export_dwg_pages` | `DWGPAGE` | igual que DXF pages | ⬜ | — |
| `export_dxfdwg_project_scheme` | `DXFDWGPROJECTSCHEME` | `export_scheme` (determina si sale DXF o DWG), `language`, `target` (default `FromSettings`) | ⬜ | El formato de salida depende 100% del scheme — no hay forma de saber si dará `.dxf` o `.dwg` sin conocer el scheme de antemano. |
| `export_dxfdwg_pages_scheme` | `DXFDWGPPAGESSCHEME` (sic, doble P — verificar que no sea typo del wrapper) | `page_names`/`page_identifiers`, `export_scheme`, `language`, `target` | ⬜ | **Revisar el nombre `DXFDWGPPAGESSCHEME`** contra la doc oficial (RAG) antes de usar — podría ser un typo en `export_.py` copiado del literal EPLAN o un bug real del wrapper. |
| `export_graphics_project` | `GRAPHICPROJECT` | `destination_path` (req), `format` (`PNG`\|`TIF`\|`GIF`\|`JPG`\|`BMP`), `color_depth`, `image_width`, `black_white`, `compression` (solo TIF) | ⬜ | Este SÍ tiene enum de formato documentado en el propio wrapper — no hace falta RAG. |
| `export_graphics_pages` | `GRAPHICPAGE` | igual + `page_name`, `use_page_filter` | ⬜ | — |
| `export_pxf_project` | `PXFPROJECT` | `export_file` (req, extensión automática), `export_masterdata` (default `True`), `export_connections` (default `False`) | ⬜ | — |
| `export_3d` | `export3d` (action distinto) | `destination_path` (req), `format`, `installation_space` | ⬜ | `format` sin enum documentado en el wrapper — consultar RAG antes de adivinar (lección de `partslist`/`label`). |

## `import_.py`

| Tool | `TYPE` interno | Parámetros clave | Estado | Notas |
|---|---|---|---|---|
| `import_pxf_project` | `PXFPROJECT` | `import_file` (req), `project_name` (req), `balance_articles`, `generate_auto_cables`, `verify` | ⬜ | 🚫 Modifica/crea proyecto destino — confirmar antes. |
| `import_dwg_page` | `DWGPAGE` | `import_file` (req), `page_name` (req), `import_scheme`, `x_scale`/`y_scale`/`x_offset`/`y_offset` | ⬜ | `import_scheme` — mismo problema de descubrimiento. |
| `import_dxf_page` | `DXFPAGE` | igual que DWG page | ⬜ | — |
| `import_dxfdwg_files` | `DXFDWGFILES` | `source_path` (req), `destination_path` (req), `import_scheme`, `macro_project`, `only_macro_project`, `code_page` (default 437) | ⬜ | No importa vía proyecto — va directo a macros. `code_page` 437 = DOS Latino US; para archivos con acentos/ñ puede necesitar 850 o 1252, revisar si da problemas. |
| `import_pdf_comments` | `PDFCOMMENTS` | `import_file` (req), `project_name` (req) | ⬜ | Docstring propio avisa: "Some settings need to be configured before importing" — no dice cuáles. Investigar con RAG antes de primer uso real. |
| `import_3d` | `import3d` (action distinto) | `import_file` (req), `import_scheme` | ⬜ | — |

## Patrón repetido en todo este grupo: el problema de los "esquemas"

Casi todas las acciones de export/import dependen de un `*_scheme` (`export_scheme`,
`import_scheme`) cuyo nombre **vive dentro de EPLAN** (Página de inicio → Utilidades →
Configuración de exportación, o equivalente) y que la LLM no puede enumerar con
ninguna tool actual. Esto es el mismo gap que causó el error de `CONFIGSCHEME` en
`label`. Ver propuestas en [TODO.md](TODO.md) — el fallback manual que funcionó fue
buscar plantillas por nombre en el filesystem de master data (`X:\Formularios`,
`X:\Plantillas`) cuando el nombre del esquema coincide con un archivo reconocible.
Para exportación (no hay archivo de plantilla necesariamente), ese truco no siempre
aplica — puede hacer falta preguntar al usuario el nombre exacto del esquema la
primera vez, y documentarlo aquí una vez confirmado.
