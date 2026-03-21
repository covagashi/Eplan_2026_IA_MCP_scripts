---
title: "ECAD objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_ecad_objects.htm"
file: "eececad_k_ecad_objects"
category: "eececad"
---

# ECAD objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## ECAD objects

The structure of an ECAD project is characterized by four ECAD objects (super classes):

     * Schematic (Super class WiringDiagram)
     * Chapter (Super class Chapter)
     * Page (Super class Page)
     * Fragment (Super class Fragment)

The hierarchy of the super classes is shown in the following figure:

Discipline components of the super classes WiringDiagram, Page and Fragment enclose files of the ECAD systems, so called Resources.

For Eplan Electric P8 these are:

Basic project template for WiringDiagram,

Page macro for Page,

Symbol macro, or window macro for Fragment.

The resource Basic project template contains all project properties, as well as the project master data, such as system libraries, plot frame, forms, etc., but no graphical content.

Discipline components of super class Chapter do not enclose any resources, they are only used for the structuring of the ECAD project. Since the structuring is largely achieved by the discipline components of super classes WiringDiagram and Page, the use of the super class Chapter is usually unnecessary.

To create the structure of an ECAD project structure identifiers are necessary, which are specified in Eplan Electric P8 by using the structure identifier management.

In the EEC in the Model variables view the names of the parameters are assigned to every possible structure identifier (see [Model variables](admin_r_modelvariables.htm) > [Disciplines](admin_r_modelvar_disciplines.htm) > [ECAD](admin_r_modelvar_ecad.htm) > [Eplan Electric P8](admin_r_modelvar_eplanp8.htm)). These parameters have to be available in the ECAD objects WiringDiagram and Page. The parameter values then determine the classification of the ECAD objects in the project structure.

### Read more

     * [Structure of the device tag](../../../../plattform/2025/content/htm/devicetaggui_k_aufbauvonbm.htm)
