---
title: "Configuring Body and Chapter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutword_h_parameterize_discipline_components_1.htm"
file: "tutword_h_parameterize_discipline_components_1"
category: "tutword"
---

# Configuring Body and Chapter

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Configuring Body and Chapter The parameters of the installed discipline components Body and Chapter still have to be provided with formulas.
    1. Select the installed components ListOfComponents.
    2. Enter the =type('T_Mechatronic_ModularSystem.Images.Logo').image formula as the value for the Logo parameter.
This formula identifies the image that is saved in the image object T_Mechatronic_ModularSystem.Images.Logo.
    1. Enter the =this.name formula as the value for the Heading parameter:
This formula is used to determine the name of the current components (Feeder).
    1. Select the installed ActuatorsTable component.
    2. Enter Actuators as the value for the Heading parameter.
    3. Select the installed Sensors_Table component.
    4. Enter Sensors as the value for the Heading parameter.
