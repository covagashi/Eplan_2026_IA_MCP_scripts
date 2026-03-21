---
title: "Creating schematics"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_schematics.htm"
file: "eececad_k_schematics"
category: "eececad"
---

# Creating schematics

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating schematics

A discipline component of the super class WiringDiagram is created via the popup menu New > ECAD > Schematic.

The effective discipline components are defined in the following editor:

The editor starts with the editor page Attributes.

A resource is assigned via [Import]. Here, as a rule a project template created in Eplan Electric P8 in the *.zw9 format is linked. Alternatively you can also link saved projects in the *.zw1 format. This linked file is used at the opening of the entire schematic or a schematic page from within EEC and contains all relevant master data and settings for the target project.

The name given automatically to the discipline component is the file name of the resource, but this can be changed manually (Note: The name must be unique within a **unit**!). The new discipline component is created by saving in the editor.

For the project structure parameters must be added to the discipline component. The parameter names are to be assigned to the respective model variables (see [Model variables](admin_r_modelvariables.htm) > [Disciplines](admin_r_modelvar_disciplines.htm) > [ECAD](admin_r_modelvar_ecad.htm) > [Eplan Electric P8](admin_r_modelvar_eplanp8.htm)).
