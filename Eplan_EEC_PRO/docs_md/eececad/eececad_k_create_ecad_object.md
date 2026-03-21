---
title: "Creating ECAD objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_create_ecad_object.htm"
file: "eececad_k_create_ecad_object"
category: "eececad"
---

# Creating ECAD objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating ECAD objects

Requirements:

     * The ECAD system library is imported into the current library.

The following sections describe the creation of the discipline component for the parent classes WiringDiagram, Chapter, Page and Fragment.

New discipline components are created via the context menu.

As good practice it is recommended to not use those discipline components directly but rather to enclose them in a mechatronic component.

Advantages of this procedure:

     * The parameter values are largely calculated on the mechatronical level, even before the discipline structure exists.
     * If the resource of a discipline component is changed or synchronized, the formulas for the calculation are then not lost.

The calculated parameter values of the mechatronics components are taken from the discipline component via a formula of the syntax =mc.$<parameter name>. To enter these so called interface parameters in a easier way, you can mark all parameters and insert them at the same time via the popup menu > Add interface parameters
