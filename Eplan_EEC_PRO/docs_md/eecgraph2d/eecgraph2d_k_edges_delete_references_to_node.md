---
title: "Deleting references to nodes"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecgraph2d_k_edges_delete_references_to_node.htm"
file: "eecgraph2d_k_edges_delete_references_to_node"
category: "eecgraph2d"
---

# Deleting references to nodes

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Deleting references to nodes

If a project component that has references to parent and/or child components is deleted from a diagram or model, references to the deleted components should also be deleted from the parent and/or child components.

The following example code defines a command with the type deleteNodeCommand which deletes the node of the type Execution (1) and additionally with the action ClearParameterReferenceAction (2) the value of the parameter with the reference to the successor (4) in the ancestor component (3).

After deletion of the node of the type Execution (1) the parameter Successor (4) in the ancestor component (3) is deleted.

If further parameter values have to be deleted, further actions with the same command must be configured.
