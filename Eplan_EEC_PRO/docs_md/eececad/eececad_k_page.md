---
title: "Creating Pages"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_page.htm"
file: "eececad_k_page"
category: "eececad"
---

# Creating Pages

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating Pages

An object of the **Page** type is created via the popup menu New > ECAD > Page.

The selection of the above action will open the following editor:

The editor of a new page is opened via the Attributes editor page.

A resource (called a window macro in the terminology of P8) is assigned to the object via [Import]. During the assignment of the resource, the file name of the resource is entered automatically as the object name. This can be modified if necessary.

If page properties are to be calculated in EEC, the page properties (except for structure identifiers and page names) must be captured via a placeholder object in the same macro.

The following figure shows the properties dialog of a placeholder object for a page in P8.

The page properties can be inserted into the table via the  (New) symbol. Then the corresponding variables can be assigned to the page properties.

An object of the Page type can be saved only if a resource has been assigned, or if the object is highlighted as abstract.

In general ECAD disciplines can be completely installed from a schematic (a component of the WiringDiagram type) and any number of pages (components of the Page type) without having to further divide the pages into fragments. Necessary variants are specified via different pages and activated/deactivated via Disabler (see [Disabler](eecbase_k_variantmanagement_disabler.htm)).
