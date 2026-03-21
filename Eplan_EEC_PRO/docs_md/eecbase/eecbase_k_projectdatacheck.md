---
title: "Checking Project Data"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_projectdatacheck.htm"
file: "eecbase_k_projectdatacheck"
category: "eecbase"
---

# Checking Project Data

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Checking Project Data

In the project data you can check whether the set selection values correspond to the actually possible selection values.

For the section of a check you can select between Workspace and Selected object.

Within a section you can further restrict the check to Parameter, Disabler or Extension points, or any other combination.

The option Check for constraint violation can be used to find parameter values which violate the specified value limits.

The check is started with Project data > Check project data. The restrictions for the section and the checking of objects can then be selected in the dialog subsequently opened.

The result is displayed in a table. All of the objects contained in it can be opened by double-clicking or using the Open popup menu entry. Marked objects are deleted from the result list and the model via the [Del] key or the popup menu entry Remove Selected Match. All of the matches are removed from the result list and the model with the Remove All Matches popup menu entry.

### Note

During the project data check, disabled objects are not considered and the formula cache is enabled.

A formula cache that is enabled requires memory.

Depending on the size of the model, the value for the memory (-xmx) in the initialization file (*.ini) has to be modified.

See [-xmx](admin_r_vmargs_xmx.htm)
