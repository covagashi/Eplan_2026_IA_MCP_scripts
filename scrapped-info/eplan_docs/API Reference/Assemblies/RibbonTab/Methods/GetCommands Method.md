# GetCommands Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonTab~GetCommands.html

---

Returns commands of a ribbon tab

Syntax

**C#**



public Dictionary<uint,string> GetCommands( 

   bool bIgnoreDummeItems

)

public:

Dictionary<uint,String^>^ GetCommands( 

   bool bIgnoreDummeItems

)


#### Parameters

*bIgnoreDummeItems*
:   Determines whether dummy commands should be ignored

#### Return Value

Commands of the ribbon tab in the form ID (key) and command text (value).
