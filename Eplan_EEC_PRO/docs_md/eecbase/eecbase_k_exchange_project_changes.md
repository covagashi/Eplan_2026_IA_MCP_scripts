---
title: "Exchanging project changes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_exchange_project_changes.htm"
file: "eecbase_k_exchange_project_changes"
category: "eecbase"
---

# Exchanging project changes

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Exchanging project changes

Project changes can be exported to a PX file (csv format separated with semicolon) or imported from such a file. During the import a project of the same name is created that contains the instances and parameter values of the PX file.

Since the exported file is in the csv format, it is possible to modify the data stored in it (e.g., in Excel) in order to configure with it a new machine or plant solely by importing the modified PX file.

The export can be started in two ways:

     * Exporting via the menu (see [Exporting project changes](eecbase_k_export_project_changes.htm)): File > Export.
     * Exporting via the projectâs context menu: Export project changes.

The import is started via the menu File > Import > Project changes ... (see [Importing project changes](eecbase_k_import_project_changes.htm)).

If after the export of project changes a change is made to the modular system, e.g., renaming library components, this will produce conflicts during the import of the original project changes. These conflicts can be solved manually by updating the PX file to be imported or automatically by means of a plug-in (see [PX update](eecbase_k_px_update.htm)).
