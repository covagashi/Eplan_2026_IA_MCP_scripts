# SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_E Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_E().html

---

Default property arrangement for variant E (alternative) # 16037.

Syntax

**C#**



public MDPropertyValue SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_E {get; set;}

public:

property MDPropertyValue^ SYMB_DEFAULT_ALTERNATIVE_PROPERTYSET_E {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Name of the alternative standard property arrangement (e.g. top right) for the GOST 2.701-84 standard. This property is used when the standard property arrangement is selected for the component and the "Use alternative property arrangement" project setting is enabled.
