# FUNC_ARTICLE_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_BACNET(Int32).html

---

BACnet # 26228.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_BACNET( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_BACNET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification whether a device or system supports the BACnet protocol. Possible specifications are, for example, the BACnet version, BACnet object types, communication interfaces or certifications. BACnet (Building Automation and Control Networks) is a data transfer protocol for building automation and building control.
