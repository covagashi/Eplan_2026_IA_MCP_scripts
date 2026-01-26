# RemoveMenuItem(ContextMenuLocation,String,String,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~RemoveMenuItem(ContextMenuLocation,String,String,Boolean,Boolean).html

---

Remove the menu item of a context menu.

Syntax

**C#**



public bool RemoveMenuItem( 

   ContextMenuLocation eContextMenuLocation,

   string strMenuName,

   string strActionName,

   bool bSeparatorBefore,

   bool bSeparatorBehind

)

public:

bool RemoveMenuItem( 

   ContextMenuLocation^ eContextMenuLocation,

   String^ strMenuName,

   String^ strActionName,

   bool bSeparatorBefore,

   bool bSeparatorBehind

)


#### Parameters

*eContextMenuLocation*
:   This is the identifier of the context menu where the new menu should removed at.

*strMenuName*
:   The name of the menu to be removed.

*strActionName*
:   Name of the [Eplan.EplApi.ApplicationFramework.Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html) to be performed when the menu item is selected. Also its parameters can be passed here.

*bSeparatorBefore*


*bSeparatorBehind*

#### Return Value

true when an item was found for this name.
