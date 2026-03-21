# ContextMenu

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu.html

---

Class for modifying context menus. Add-ins can add new context menu items to the EPLAN context menu. A menu item is connected to an [Eplan.EplApi.ApplicationFramework.Action](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.Action.html).

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Gui.ContextMenu**

Syntax

**C#**



public class ContextMenu

public ref class ContextMenu


Example

Example creating a contextmenu:

- [c#](#i-tab-content-e8720095-4058-49e7-ad6b-976c7db7024e)

```
ContextMenuLocation oLocation = new ContextMenuLocation();

oLocation.DialogName = "Editor";

oLocation.ContextMenuName = "Ged";

ContextMenu oTestMenu = new ContextMenu();

oTestMenu.AddMenuItem(oLocation, "My Contextmenuname",

	"MyFavoriteActionName", true, false));
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ContextMenu Constructor](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~_ctor.html) | Creates a new object. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddMenuItem](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~AddMenuItem.html) | Adds a new menu item at the end of a context menu. |
| Public Method | [GetMenuItem](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~GetMenuItem.html) | Get the menu item of a context menu from the index. |
| Public Method | [GetMenuItemCount](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~GetMenuItemCount.html) | Get the count of added menu items of a context menu. |
| Public Method | [RemoveMenuItem](Eplan.EplApi.Guiu~Eplan.EplApi.Gui.ContextMenu~RemoveMenuItem.html) | Overloaded. Remove the menu item of a context menu. |


