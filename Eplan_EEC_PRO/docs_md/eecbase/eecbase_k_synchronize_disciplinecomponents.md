---
title: "Synchronization of discipline components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_synchronize_disciplinecomponents.htm"
file: "eecbase_k_synchronize_disciplinecomponents"
category: "eecbase"
---

# Synchronization of discipline components

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Synchronization of discipline components

If the resource of a discipline component has been changed, for example extended with an additional parameter, the discipline component should be synchronized with the changes.

If the resource is stored externally, the synchronization can be started through the following actions:

     * Select a library, unit or discipline component Popup menu > Synchronize external resources....
     * Open the discipline component, click [Synchronization...] in the Attributes editor.

If the resource is stored internally, the synchronization is started through the following action:

     * Open the discipline component, click [Update & Synchronize] in the Attributes editor. In this action, the internal resource is first replaced by the external resource and then the data in the model is synchronized.

The action opens the Synchronization view in which all discipline components are listed that were changed. Double-clicking the changed discipline component opens the comparison editor. In it the parameters of the discipline component are listed before and after the synchronization.

     * Parameters unchanged in the resource are grayed out.
     * Parameters removed in the resource are crossed out.
     * Parameters added in the resource are represented as normal.
     * For P8 macros the macro description before and after the synchronization.

By saving the editor the changes represented in the Parameters after synchronization: list are applied.

### Note

If an external resource is synchronized for an ECAD discipline component, the synchronization view opens. The name field displays the absolute name of the discipline component to be synchronized. To navigate to the discipline component, the absolute name must be copied to the clipboard and inserted into the library catalog. In the library catalog, the tree for the discipline component is opened and the searched discipline component is selected.
