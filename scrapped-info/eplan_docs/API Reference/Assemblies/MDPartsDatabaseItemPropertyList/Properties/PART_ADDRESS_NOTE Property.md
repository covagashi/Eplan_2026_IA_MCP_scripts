# PART_ADDRESS_NOTE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~PART_ADDRESS_NOTE().html

---

Description (address) # 22922.

Syntax

**C#**



public MDPropertyValue PART_ADDRESS_NOTE {get; set;}

public:

property MDPropertyValue^ PART_ADDRESS_NOTE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Descriptive text for a customer, manufacturer or supplier in the parts management. This property is used for entering internal information or remarks, e.g. "responsible for sales, part....., good credit, etc." and so on.
