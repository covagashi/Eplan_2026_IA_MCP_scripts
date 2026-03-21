# Commands Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~Commands.html

---

Returns commands of the command group

Syntax

**C#**



public Dictionary<uint,RibbonCommand> Commands {get;}

public:

property Dictionary<uint,RibbonCommand^>^ Commands {

   Dictionary<uint,RibbonCommand^>^ get();

}


#### Property Value

Returns commands of the command group in the form ID (key) and a RibbonCommand (value). Ignores dummy items.
