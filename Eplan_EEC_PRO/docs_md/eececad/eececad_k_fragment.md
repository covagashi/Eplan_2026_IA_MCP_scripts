---
title: "Creating fragments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_fragment.htm"
file: "eececad_k_fragment"
category: "eececad"
---

# Creating fragments

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Creating fragments

An object of the **Fragment** type is created in a way similar to that of the Page object. Use the popup menu to select New > ECAD > Fragment.

The above selection opens the Fragment object with the Attributes editor page:

The name field is highlighted in red as long as no valid name has been entered. The name must be unique within a unit. During the assignment of a resource, the file name of the resource is entered automatically as the object name. This can be modified if necessary. Saving the editor creates the new fragment.

A file of an Eplan Electric P8 window macro is assigned to the object as a resource via [Import]. In this macro, it would not make sense to define page properties as parameters, because page properties cannot be defined via a fragment. Only one Plug may be defined in an Eplan Electric P8 window macro. Further Sockets can be defined to place further fragments on the fragment.

An object of the Fragment type can be saved only if a resource has been assigned, or if the object is highlighted as abstract.
