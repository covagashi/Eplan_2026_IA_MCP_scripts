# FUNC_CONNECTIONDIMENSIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CONNECTIONDIMENSIONS(Int32).html

---

Connection dimension # 20374.

Syntax

**C#**



public PropertyValue FUNC_CONNECTIONDIMENSIONS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_CONNECTIONDIMENSIONS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
