# 01 — Proyecto, Workspace, Backup/Restore

Ver leyenda de estado en [00-INDEX.md](00-INDEX.md).

## `project.py`

| Tool | Acción EPLAN | Parámetros MCP | Estado | Notas |
|---|---|---|---|---|
| `open_project` | `ProjectOpen` | `project_path` (req), `open_mode` (`Standard`\|`ReadOnly`\|`Exclusive`) | ⬜ | — |
| `close_project` | `XPrjActionProjectClose` | — | ⬜ | 🚫 Cierra sin preguntar — **confirmar con el usuario si hay cambios sin guardar** (ver `llm.md` §7). |
| `project_management` | `projectmanagement` | `type` (req: `READPROJECTINFO`\|`PUBLISHSMARTPRODUCTION`\|`CREATESNAPSHOTCOPY`\|`EXPORTPROPERTYPLACEMENTSSCHEMAS`\|`IMPORTPROPERTYPLACEMENTSSCHEMAS`\|`REORGANIZE`\|`CORRECTPROJECTITEMS`\|`LOADDIRECTORY`), `project_name`, `filename`, `scheme`, `overwrite`, `extended_mode`, `projects_directory`, `scan_subdirectories` | ⬜ | `scheme` — mismo problema potencial que `CONFIGSCHEME`: no hay forma de listar los schemes disponibles sin abrir la GUI. Probar `READPROJECTINFO` primero (parece read-only y buen candidato para descubrir campos). |
| `upgrade_projects` | `XPrjActionUpgradeProjects` | `project_paths` (lista) | ⬜ | 🚫 Irreversible sobre la versión de esquema del proyecto — confirmar antes. |
| `compress_project` | `compress` | `project_name` | ⬜ | — |
| `synchronize_project` | `synchronize` | `project_name` | ⬜ | — |
| `get_current_project` | `selectionset /TYPE:PROJECT` | — | ⬜ | Usado de forma indirecta en sesión previa bajo el servidor viejo (v1/v2) — pendiente reverificar con la tool unificada `eplan_get_current_project`. |
| `set_project_language` | `SetProjectLanguage` | `language` (req), `project_name`, `read_write` (default `True`) | ⬜ | Ojo: mismo tipo de parámetro `LANGUAGE` que falló en `label` por venir vacío — aquí es obligatorio en la firma Python así que no debería repetirse el problema. |
| `switch_project_type` | `SwitchProjectType` | `project_type` (req), `project_name` | ⬜ | 🚫 Cambia el tipo de proyecto — confirmar antes. |

## `workspace.py`

> ⚠️ El propio código advierte: necesitan mainframe/GUI. Bajo QuietMode remoto pueden no comportarse igual que en modo interactivo (`llm.md` §6 lo marca como gotcha conocido).

| Tool | Acción EPLAN | Parámetros MCP | Estado | Notas |
|---|---|---|---|---|
| `open_workspace` | `OpenWorkspaceAction` | `workspace_name` (req; **`"?"` lista todos los workspaces disponibles** — útil para descubrir nombres sin preguntar al usuario), `silent` | ⬜ | Probar primero con `workspace_name="?"` para inventariar antes de abrir uno real. |
| `save_workspace` | `SaveWorkspaceAction` | `workspace_name` (req), `silent` | ⬜ | 🚫 Sobrescribe/crea workspace — confirmar nombre con el usuario si no es evidente cuál. |
| `clean_workspace` | `CleanWorkspaceAction` | `workspace_name` (si se omite, limpia el `LAST_USED`), `silent` | ⬜ | 🚫 Destructivo sobre el workspace — confirmar antes, y **nunca omitir `workspace_name`** sin saber cuál es el "last used" real. |

## `backup.py`

| Tool | Acción EPLAN | Parámetros MCP | Estado | Notas |
|---|---|---|---|---|
| `backup_project` | `backup /TYPE:PROJECT` | `destination_path` (req), `archive_name` (req), `project_name`, `comment`, `auto_copy_ref_data`, `include_ext_docs`, `include_images`, `backup_method` (`BACKUP`\|`SOURCEOUT`\|`ARCHIVE`) | ⬜ | — |
| `backup_masterdata` | `backup /TYPE:MASTERDATA` | `destination_path` (req), `archive_name` (req), `source_path` (req), `md_type` (req: `SYMBOLS`\|`MACROS`\|`FORMS`\|`ARTICLES`\|`LANGUAGES`\|`STANDARDSHEET`\|`STATIONDATA`), `filename` (default `*.*`), `comment` | ⬜ | `source_path` — usar `pathmap_get_common_paths` primero para obtener `$(MD_SYMBOLS)`, `$(MD_FORMS)`, etc. en vez de adivinar la ruta. |
| `restore_project` | `restore /TYPE:PROJECT` | `archive_name` (req), `project_name` (req), `unpack_project`, `restore_project_info` (default `True`) | ⬜ | 🚫 Sobrescribe destino — confirmar antes (`llm.md` §7: "restore/backup overwrites"). |
| `restore_masterdata` | `restore /TYPE:MASTERDATA` | `archive_name` (req), `destination_path` (req) | ⬜ | 🚫 Igual que arriba, confirmar antes. |

## Contexto que le falta a la LLM en este grupo

- **Nombres de scheme para `project_management` (`scheme`)** — no hay tool para listarlos.
  Candidato de investigación: si `TYPE:READPROJECTINFO` es read-only, probarlo primero
  sin `scheme` para ver qué información expone antes de tocar `REORGANIZE`/`CORRECTPROJECTITEMS`.
- **`open_workspace(workspace_name="?")`** es la única acción de este grupo que
  documenta explícitamente su propio mecanismo de auto-descubrimiento — usarlo antes
  de pedirle el nombre al usuario.
