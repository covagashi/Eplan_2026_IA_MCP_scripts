# FUNC_CATEGORY_REGION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~FUNC_CATEGORY_REGION().html

---

Function definition: Area # 20088.

Syntax

**C#**



public MDPropertyValue FUNC_CATEGORY_REGION {get; set;}

public:

property MDPropertyValue^ FUNC_CATEGORY_REGION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only..

Area for grouping the function definitions. Provides the area within the trade, e.g., "coils and contacts" or "motors".
