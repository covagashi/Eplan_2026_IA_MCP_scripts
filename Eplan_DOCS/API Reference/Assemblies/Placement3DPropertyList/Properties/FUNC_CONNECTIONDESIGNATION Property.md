# FUNC_CONNECTIONDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CONNECTIONDESIGNATION(Int32).html

---

Function: Connection point designation # 20022.

Syntax

**C#**



public PropertyValue FUNC_CONNECTIONDESIGNATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_CONNECTIONDESIGNATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the connection point designations of the function. The index can be used to define a max. of 100 sets of connection point designations.
