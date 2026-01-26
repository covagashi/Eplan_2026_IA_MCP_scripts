# InsertMacroBox Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~InsertMacroBox.html

---

Gets or sets insert macro box property.

Syntax

**C#**



public MacroBox.Enums.InsertMacroBox InsertMacroBox {get; set;}

public:

property MacroBox.Enums.InsertMacroBox InsertMacroBox {

   MacroBox.Enums.InsertMacroBox get();

   void set (    MacroBox.Enums.InsertMacroBox value);

}


Remarks

Property determines if macro box should be inserted. There are some exceptions i.e. preplanning macros, macro projects (macro box is always inserted). When property is set to [MacroBox.Enums.InsertMacroBox.FromProjectSettings](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox+Enums+InsertMacroBox.html), "Project->{Project name}->Graphical editing->General->Also insert macro boxes" checkbox is considered.
