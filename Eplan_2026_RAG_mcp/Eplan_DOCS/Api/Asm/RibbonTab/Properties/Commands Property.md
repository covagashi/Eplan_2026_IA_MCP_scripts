# Commands Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonTab~Commands.html

---

Returns all commands of a ribbon tab (as texts)

Syntax

**C#**



public Dictionary<uint,string> Commands {get;}

public:

property Dictionary<uint,String^>^ Commands {

   Dictionary<uint,String^>^ get();

}


#### Property Value

Commands of the ribbon tab in the form ID (key) and command text (value). Ignores dummy items.
