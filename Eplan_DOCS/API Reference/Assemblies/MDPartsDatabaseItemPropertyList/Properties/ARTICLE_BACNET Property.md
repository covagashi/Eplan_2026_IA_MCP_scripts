# ARTICLE_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_BACNET().html

---

BACnet # 26227.

Syntax

**C#**



public MDPropertyValue ARTICLE_BACNET {get; set;}

public:

property MDPropertyValue^ ARTICLE_BACNET {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specification whether a device or system supports the BACnet protocol. Possible specifications are, for example, the BACnet version, BACnet object types, communication interfaces or certifications. BACnet (Building Automation and Control Networks) is a data transfer protocol for building automation and building control.
