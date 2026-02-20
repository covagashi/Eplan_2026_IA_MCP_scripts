# FUNC_ARTICLE_CONNECTION_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_CONNECTION_TYPE(Int32).html

---

Connection point type # 26205.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CONNECTION_TYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CONNECTION_TYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Physical design of the connection point via which an electrical device can be connected. The way in which a motor is connected in the circuit. Type of wiring used to connect the connection cable to the device.
