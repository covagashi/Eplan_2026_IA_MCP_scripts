---
title: "Instance name parameter for discipline structures"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_nameofdiscipline.htm"
file: "admin_r_modelvar_nameofdiscipline"
category: "admin"
---

# Instance name parameter for discipline structures

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Instance name parameter for discipline structures

Path to model variable:

Disciplines

Specify the name of a parameter. Add this parameter to the root projects of the disciplines. The value of the parameter in the discipline components defines the name of a discipline root project.

### [Example for the discipline ECAD](javascript:void\(0\);)

    1. Create the Disciplineroot parameter with the Stringtype.
    2. Add this parameter to a discipline component of the WiringDiagram type.
    3. For this parameter, enter the value Schematic.
    4. Create the project and create the ECAD discipline structure.

The root project with the name Schematic is located in the project structure below ECAD.
