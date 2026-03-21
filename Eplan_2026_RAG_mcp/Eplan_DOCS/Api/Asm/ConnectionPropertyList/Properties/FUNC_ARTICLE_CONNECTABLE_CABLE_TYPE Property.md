# FUNC_ARTICLE_CONNECTABLE_CABLE_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CONNECTABLE_CABLE_TYPE(Int32).html

---

Connectable cable type # 31179.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CONNECTABLE_CABLE_TYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CONNECTABLE_CABLE_TYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Cable type that can be connected to a device. The cable type describes the physical properties of the cable.
