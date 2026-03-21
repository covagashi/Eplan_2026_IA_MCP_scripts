---
title: "Actions and methods"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_actions.htm"
file: "eecplc_k_actions"
category: "eecplc"
---

# Actions and methods

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Actions and methods

Actions are contained in the resources of the components of the types SourceProgram (program), SourceFunctionBlock (function block) or SourceFunction (Function), Methods only in the components of the type SourceFunctionBlock (function block).

For the creation of a discipline component whose resource contains actions or methods, the actions or methods are automatically created as standalone child components. These child components have no resources, but are a reference to the action/method that is contained in the resource of the parent discipline component.

In the mechatronic structure of a project, the actions/methods can be located under any mechatronic component.

After generating the discipline structure, the actions/methods must be placed under a POU in accordance with the Plug-Socket principle.

When the code is created, actions and methods are added into the code of a discipline component only when these are present in the discipline structure under a discipline component. If a discipline component in the library contains an action/method, but not in the discipline structure of the project, the action/method is removed from the code of the created project component.

On the other hand, the action/method that is located in the discipline structure under the discipline component is added to the code of each created discipline component.

During the import of a resource for a discipline component, all necessary parameters are automatically created and allocated to the discipline component. This applies, in general, also for the parameters of an action, but with the difference that the necessary parameters of an action are not the action itself, but instead are allocated to the discipline component containing them. Additional parameters can also be allocated to an action by hand.
