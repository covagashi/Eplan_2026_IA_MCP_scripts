---
title: "Creating a root component of the discipline"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutpropanel_h_create_root_component.htm"
file: "tutpropanel_h_create_root_component"
category: "tutpropanel"
---

# Creating a root component of the discipline

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Creating a root component of the discipline An ECAD discipline component of the type WiringDiagram also serves as a root component for the Pro Panel discipline. A resource is only assigned to this discipline component. All discipline components arranged below this have no resources but reference 3D graphics macros of the Eplan parts database. Create the root component:
    1. Select the ProPanel unit.
    2. From the popup menu, select New > ECAD > Schematic.
    3. Click [Assign].
    4. Select the <EEC installation folder>\resources\ECAD\IEC_bas001.zw9 file.
    5. Enter WiringDiagram as the name.
    6. Save the editor using [Ctrl] \+ [S].
In this process, the ECAD.Parameter unit was created in addition (see [ECAD Parameter Unit](admin_r_modelvar_ecad_parameterunit.htm)). This contains the following parameters: FunctionDesignation, LocationDesignation, ProjectSupplementaryFields, Report, Script and ScriptArguments. The names of the parameters can be set under Model > Model Variables (see [Model variables](admin_r_modelvariables.htm)).
