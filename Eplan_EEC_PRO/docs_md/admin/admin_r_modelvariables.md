---
title: "Model variables"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvariables.htm"
file: "admin_r_modelvariables"
category: "admin"
---

# Model variables

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Model variables

Path to the dialog:

Model > Model variables

Discipline-specific variables can be configured in a user-specific manner as part of customizing EEC. Apart from parameter names, it is also possible to define the procedure for the import of external resources.

Model variables can be exported to files with the extensions .mdv and imported again to a model .

During the import, only the model variables are overwritten that are contained in the *.mdv file. If all other model variables are to be reset to their defaults, select the check box Reset model variables that are not contained in import file to default values (see the following figure).

There are two ways of doing this:

    1. Importing and exporting without open model variables editor:

Export: File > Export... > Model > Model Variables

Import: File > Import... > Model > Model Variables

All currently stored model variables are exported; during the import, all existing model variables are overwritten and stored.

    2. Importing and exporting in the model variables editor:

Export: using icon  or Popup Menu > Export

Import: using icon  or Popup Menu > Import

Only highlighted model variables are exported. This takes into account also model variables that have not yet been saved. In the import, only model variables are overwritten that were imported from the *.mdv file. The imported model variables are not saved automatically; this must be done separately.
