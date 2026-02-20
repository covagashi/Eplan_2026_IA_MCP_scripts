# RemoveMenuItem(ContextMenuLocation,UInt32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~RemoveMenuItem(ContextMenuLocation,UInt32).html

---

Remove the menu item of a context menu of the index.

Syntax

**C#**



public bool RemoveMenuItem( 

   ContextMenuLocation contextMenuLocation,

   uint nIndex

)

public:

bool RemoveMenuItem( 

   ContextMenuLocation^ contextMenuLocation,

   uint nIndex

)


#### Parameters

*contextMenuLocation*
:   This is the identifier of the context menu

*nIndex*
:   the zero based index of the menu item.

#### Return Value

true when an item was found for this index.
