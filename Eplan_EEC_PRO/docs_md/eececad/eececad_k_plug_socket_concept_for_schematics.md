---
title: "Plug-socket concept in the schematic"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_plug_socket_concept_for_schematics.htm"
file: "eececad_k_plug_socket_concept_for_schematics"
category: "eececad"
---

# Plug-socket concept in the schematic

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Plug-socket concept in the schematic

The conceptual approach of the plug-socket concept is explained in the section [Plug-Socket concept](concept_k_plug_socket_concept.htm). The following section explains the use of the concept with Eplan Electric P8.

The plug-socket concept fulfills two functions in the context of the ECAD discipline. On the one hand, it can be used to describe a discipline-specific structure (logical placement), and on the other hand, it represents the correctly positioned placement of the macros / fragments to each other (graphical placement).

Logical placement:

The logical link between the electro-technical objects is established by way of the **plug-socket concept**. For example, if a page has a socket, different plugs within a project can reference it. This results in a logical, discipline-specific project structure. When the ECAD structure is created, the ECAD objects are placed logically.

Graphical placement:

The plug-socket concept is also used to arrange fragments with partial circuits in the correct position to each other on a schematic page. **Sockets** represent the placeholder for fragments in this case. Fragments can be docked to these placeholders. On a fragment, a plug represents the handle. In the placement, the extension points of the free texts of the socket and the plug are aligned with each other. This is done while generating and opening the Eplan Electric P8 project from within the ECAD structure.

### Notes

     * No plug may be placed on one page.
     * Only one plug may be placed on one fragment.
     * Any number of sockets can be placed on pages and fragments.

Plugs and sockets are entered in the schematics as free text, and included only in the macro content, but not in a placeholder object. By importing the macro as a resource, they become the parameter of the respective ECAD object. The data type of the parameter is, then, Socket or Plug.

Plug:

Syntax:
    
        #<Plug:Parametername>

Example:

Socket:

Syntax:
    
        #<Socket:Parametername>

Example:

When opening a schematic, plugs and sockets are connected to each other. Here, the graphical elements of the resources concerned are arranged in such a way that the extension points of the text elements Socket and Plug lie perfectly on top of each other. Socket and Plug are not created from the parameter name, but from the values set in the parameters. In Eplan Electric P8, connections are created automatically via the integrated "Autoconnecting" function.

Please note that the calculated values of plugs and sockets in the mechatronic structure may sometimes differ from those in the discipline structure. For example, the **this** method yields different values. If **this** is used as an argument in the method **indexOf()** , it is possible that the result delivers a value of -1 (not found) in the discipline if the collection to which the method is applied does not contain the ECAD structure object.
