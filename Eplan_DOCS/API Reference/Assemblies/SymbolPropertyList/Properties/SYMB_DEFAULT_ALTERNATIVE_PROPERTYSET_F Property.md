# SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_F Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_F().html

---

Default property arrangement for variant F (alternative) # 16038.

Syntax

**C#**



public PropertyValue SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_F {get; set;}

public:

property PropertyValue^ SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_F {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Name of the alternative standard property arrangement (e.g. top right) for the GOST 2.701-84 standard. This property is used when the standard property arrangement is selected for the component and the "Use alternative property arrangement" project setting is enabled.
