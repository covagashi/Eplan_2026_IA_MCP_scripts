# ARTICLE_VOLTAGETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_VOLTAGETYPE().html

---

Voltage type # 22070.

Syntax

**C#**



public MDPropertyValue ARTICLE_VOLTAGETYPE {get; set;}

public:

property MDPropertyValue^ ARTICLE_VOLTAGETYPE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Used for the entry of the voltage type (AC / DC). At a part with the product group "Relays, contactors" this property refers to the coil.
