# SYMB_SAFETYRELEVANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_SAFETYRELEVANT().html

---

Safety function # 16044.

Syntax

**C#**



public PropertyValue SYMB_SAFETYRELEVANT {get; set;}

public:

property PropertyValue^ SYMB_SAFETYRELEVANT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Shows whether a function that is relevant to safety is generated when placing and replacing a symbol. The visibility of the property depends on the type of symbol. The following values are possible:

0 = Not defined (the property is not observed when placing and replacing the symbol).

1 = Yes (a function that is relevant to safety is created for this symbol when placing and replacing the symbol).

2 = No (a function that is not relevant to safety is created for this symbol when placing and replacing the symbol).
