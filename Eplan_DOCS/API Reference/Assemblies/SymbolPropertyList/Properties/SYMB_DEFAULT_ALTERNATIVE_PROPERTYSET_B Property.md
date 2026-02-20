# SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_B Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_B().html

---

Default property arrangement for variant B (alternative) # 16034.

Syntax

**C#**



public PropertyValue SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_B {get; set;}

public:

property PropertyValue^ SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_B {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Name of the alternative standard property arrangement (e.g. top right) for the GOST 2.701-84 standard. This property is used when the standard property arrangement is selected for the component and the "Use alternative property arrangement" project setting is enabled.
