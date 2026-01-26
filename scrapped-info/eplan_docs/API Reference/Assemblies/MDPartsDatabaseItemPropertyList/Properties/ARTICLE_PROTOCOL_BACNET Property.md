# ARTICLE_PROTOCOL_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PROTOCOL_BACNET().html

---

BACnet: Protocol # 26540.

Syntax

**C#**



public MDPropertyValue ARTICLE_PROTOCOL_BACNET {get; set;}

public:

property MDPropertyValue^ ARTICLE_PROTOCOL_BACNET {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specification that a device or system supports the BACnet protocol. Example: The "BACnet/IP" specification means that the device supports the BACnet protocol over IP networks.
