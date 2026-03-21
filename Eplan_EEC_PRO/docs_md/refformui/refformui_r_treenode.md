---
title: "treeNode"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_treenode.htm"
file: "refformui_r_treenode"
category: "refformui"
---

# treeNode

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  treeNode The <treeNode> element defines subordinate project components to be displayed in the tree structure. Which project components should be displayed is defined by a formula that creates a list of project components. The list should be sent to the children attribute. The names of the project components can either be received directly or manipulated with the aid of the name attribute. If an icon is to be displayed in front of every entry, this can be specified via the icon attribute. This element has no sub-elements. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
children | optional |  | Directly subordinate project components | The specified formula must create a list of project components.  
icon | optional |  |  | Picture displayed in front of an entry in the tree structure.  
name | optional |  | Name of the project component. | The specified formula must yield a project component that serves as the root of the tree structure.
