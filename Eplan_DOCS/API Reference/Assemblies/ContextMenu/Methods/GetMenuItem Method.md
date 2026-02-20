# GetMenuItem Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~GetMenuItem.html

---

Get the menu item of a context menu from the index.

Syntax

**C#**



public bool GetMenuItem( 

   ContextMenuLocation contextMenuLocation,

   uint nIndex,

   ref string strMenuName,

   ref string strActionName,

   ref bool bIsSeparator

)

public:

bool GetMenuItem( 

   ContextMenuLocation^ contextMenuLocation,

   uint nIndex,

   String^% strMenuName,

   String^% strActionName,

   bool% bIsSeparator

)


#### Parameters

*contextMenuLocation*
:   This is the identifier of the context menu

*nIndex*
:   the zero based index of the menu item.

*strMenuName*
:   The name of the menu returned.

*strActionName*
:   The name of the action returned.

*bIsSeparator*
:   returnes true when this menu item is a separator.

#### Return Value

true when an item was found for this index.
