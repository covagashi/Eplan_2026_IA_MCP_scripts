# FUNC_ARTICLE_PROTOCOL_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_PROTOCOL_BACNET(Int32).html

---

BACnet: Protocol # 26541.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PROTOCOL_BACNET( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PROTOCOL_BACNET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification that a device or system supports the BACnet protocol. Example: The "BACnet/IP" specification means that the device supports the BACnet protocol over IP networks.
