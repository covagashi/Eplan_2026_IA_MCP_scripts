# FUNC_ARTICLE_TORQUE_AT_MIN_SPEED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_TORQUE_AT_MIN_SPEED(Int32).html

---

Torque (at min. rotation speed) # 26252.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TORQUE_AT_MIN_SPEED( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TORQUE_AT_MIN_SPEED {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Torque at the minimum permissible output speed of the drive engine.
