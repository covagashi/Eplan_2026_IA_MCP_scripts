---
title: "Exporting project changes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_export_project_changes.htm"
file: "eecbase_k_export_project_changes"
category: "eecbase"
---

# Exporting project changes

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Exporting project changes

The following sequence describes how to export project changes to a PX file.

    1. Highlight the project whose changes you wish to export.
    2. Select Export project changes from the popup menu.

The Export Project Changes dialog opens.

    1. Enter a file name for the PX file.
    2. If necessary, correct the selection of the project whose changes you want to export.
    3. If necessary, mark the check box Including extension points.

Option Including extension points marked: Components placed on extension points are also exported. The extension points are not updated during the import process. If no components are placed on the extension points, a PX file as small as possible is created. The update of the extension points then has to be executed explicitly.

Option Including extension points not marked: Components placed on extension points are not exported. The extension points are updated during the import process. With this option it is not possible to remove components which are already placed on extension points via PX-Import.

    1. Click [Finish].

Since the export file is in the csv format, it can be opened and modified with any editor, for example, Excel (see the following figure).

The parameter values are stored in the PX file without an annotation, because the annotations lose their validity in a new project anyway. In addition, the readability of the exported data is improved.
