# FUNC_LOGDEF_SAFETYISPOSSIBLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_LOGDEF_SAFETYISPOSSIBLE(Int32).html

---

Connection point logic: Intrinsic safety possible # 20323.

Syntax

**C#**



public PropertyValue FUNC_LOGDEF_SAFETYISPOSSIBLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_SAFETYISPOSSIBLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Specifies whether the connection point can be intrinsically safe. If it is later specified in the function that it is intrinsically safe, then all connection points will be intrinsically safe for which this property is selected. Using the index, you can differentiate between up to 100 settings.
