# ARTICLE_VOLTAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_VOLTAGE().html

---

Voltage # 22033.

Syntax

**C#**



public MDPropertyValue ARTICLE_VOLTAGE {get; set;}

public:

property MDPropertyValue^ ARTICLE_VOLTAGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Coil operating voltage or of the component (connection point voltage for electricity consumers). At a part with the product group "Relays, contactors" this property refers to the coil.
