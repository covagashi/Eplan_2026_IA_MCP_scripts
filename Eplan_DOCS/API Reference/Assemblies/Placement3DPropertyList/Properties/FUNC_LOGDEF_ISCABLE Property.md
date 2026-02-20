# FUNC_LOGDEF_ISCABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_LOGDEF_ISCABLE(Int32).html

---

Connection point logic: Cable connection point # 20322.

Syntax

**C#**



public PropertyValue FUNC_LOGDEF_ISCABLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_ISCABLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Defines whether the connection should lie in a cable. This setting is taken into account when automatically generating cables. Using the index, you can differentiate between up to 100 settings.
