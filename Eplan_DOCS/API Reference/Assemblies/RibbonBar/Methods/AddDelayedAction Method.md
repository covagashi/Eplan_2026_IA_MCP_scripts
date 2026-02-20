# AddDelayedAction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddDelayedAction.html

---

Calls an action object on the ribbon. If the ribbon doesn't exist yet, the action will be executed after the system start is finished

Syntax

**C#**



public void AddDelayedAction( 

   Action<RibbonBar> action

)

public:

void AddDelayedAction( 

   Action<RibbonBar^>^ action

)


#### Parameters

*action*
:   The action object to be executed
