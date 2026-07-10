# 07 — Renumerar, Capas, Traducción, Impresión

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md).

## `renumber.py`

🚫 **Todo este módulo es destructivo/irreversible sobre designaciones del proyecto**
(`llm.md` §7 ya lo marca explícitamente) — **confirmar con el usuario antes de
ejecutar cualquiera de estas**, incluso en modo auto.

| Tool | `TYPE` | Parámetros propios más relevantes | Estado | Notas |
|---|---|---|---|---|
| `renumber_devices` | `DEVICES` | `start_value`, `step_value`, `config_scheme`, `filter_scheme`, `identifier` (patrón ej. `"X*"`, `"V"`), `use_selection`, `post_numerate` (default `True` = solo renumera tags inválidos "?"), `also_numerated_by_plc`, `numerate_cables` | ⬜ | 🚫 `post_numerate=True` por defecto es relativamente seguro (no toca tags ya válidos); si el usuario quiere renumerar TODO, hay que poner `post_numerate=False` explícitamente y eso sí es de alto impacto. |
| `renumber_pages` | `PAGES` | `structure_oriented`, `keep_interval`, `keep_text`, `subpages` (0=mantener,1=numeración consecutiva,2=convertir en páginas principales) | ⬜ | 🚫 |
| `renumber_cables` | `CABLES` | `config_scheme`, `keep_existing`, `keep_identifier` | ⬜ | 🚫 |
| `renumber_terminals` | `TERMINALS` | Muchísimos parámetros (`sequence`, `extent`, `prefix`, `suffix`, `potential_n/pe/sh`, `multiple_terminals`, `keep_alpha`...) — el más complejo del módulo | ⬜ | 🚫 Antes del primer uso real, confirmar cada flag no evidente con el usuario o el RAG; alta probabilidad de resultado no deseado si se asumen defaults sin revisar. |
| `renumber_connections` | `CONNECTIONS` | `groups` (dict de grupos con `start`/`step` por grupo — sintaxis propia del wrapper, no 1:1 con la doc EPLAN), `overwrite` (0=todo,1=excepto manuales,2=nada), `avoid_identical_designations`, `visibility`, `mark_as_manual` | ⬜ | 🚫 El parámetro `groups` es una traducción del wrapper (`/GROUP_n`, `/STARTVALUE_n`, `/STEPVALUE_n`) — verificar contra RAG que el mapeo sea correcto antes de confiar en él a ciegas. |

Todos comparten `CONFIGSCHEME` opcional (excepto `renumber_pages`) — mismo patrón de
descubrimiento pendiente que en el resto del audit.

## `layers.py`

| Tool | Acción EPLAN | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `change_layer` | `changelayer` | `layer_name`, `visible`, `printed`, `text_height`, `color_id`, `transparency`, `project_name` | ⬜ | 🚫 Modifica una capa gráfica global del proyecto — confirmar antes, especialmente si `layer_name` no viene de una lista conocida (no hay tool para listar capas existentes). |
| `export_graphical_layer_table` | `graphicallayertable /TYPE:EXPORT` | `export_file` (req), `project_name` | ⬜ | Read-only, buen candidato de test temprano — y además sirve para **descubrir los nombres de capa reales** antes de usar `change_layer`. |
| `import_graphical_layer_table` | `graphicallayertable /TYPE:IMPORT` | `import_file` (req), `project_name` | ⬜ | 🚫 Confirmar antes. |

## `translate.py`

| Tool | `TYPE` | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `translate_project` | `TRANSLATEPROJECT` | `project_name` | ⬜ | 🚫 Modifica textos del proyecto vía BD de traducción — confirmar antes. |
| `export_missing_translations` | `EXPORTMISSINGTRANSLATIONS` | `export_file` (req), `language` (req), `project_name`, `converter` | ⬜ | Read-only, seguro de probar. `converter` sin enum documentado — si falla, RAG antes de adivinar (ya sabemos el costo de adivinar `FORMAT`/`converter`). |
| `remove_language` | `REMOVELANGUAGE` | `language` (req, admite lista `"en_US,fr_FR"`), `project_name` | ⬜ | 🚫 Irreversible sobre datos multi-idioma — confirmar antes. |

## `print_.py`

| Tool | `TYPE` | Parámetros | Estado | Notas |
|---|---|---|---|---|
| `print_project` | `PROJECT` | `printer_name` (si se omite, usa la predeterminada del sistema), `copies`, `collate`, `reverse`, `destination_file` (imprime a archivo en vez de impresora física) | ⬜ | 🚫 Con `destination_file` es de bajo riesgo (no consume papel/impresora real); **sin** él, imprime físicamente — confirmar siempre que no se use `destination_file`, y preferir siempre pasarlo en pruebas. |
| `print_pages` | `PAGES` | `page_name`, `printer_name`, `copies`, `use_page_filter`, `print_changed_only` | ⬜ | 🚫 No tiene `destination_file` en este wrapper (a diferencia de `print_project`) — toda invocación va a una impresora física/predeterminada. Confirmar siempre antes de usar. |

## Contexto que le falta a la LLM en este grupo

- **Ninguna tool para listar impresoras disponibles** — si el usuario no da
  `printer_name`, se usa la predeterminada del sistema, que puede no ser la deseada
  (ej. imprimir a una impresora física por accidente en vez de a PDF). Recomendado:
  siempre preguntar o usar `destination_file` en `print_project` cuando sea posible.
- **Ninguna tool para listar capas** salvo `export_graphical_layer_table` (que exporta
  a archivo, hay que leerlo después) — es el flujo correcto para descubrir
  `layer_name` antes de `change_layer`, documentarlo como práctica estándar.
- El parámetro `groups` de `renumber_connections` es una **traducción propia del
  wrapper** (no un parámetro EPLAN 1:1) — es el único caso detectado en todo el audit
  donde el MCP inventa su propia sintaxis sobre la acción real; verificar con cuidado
  contra la doc EPLAN antes de confiar en la traducción.
