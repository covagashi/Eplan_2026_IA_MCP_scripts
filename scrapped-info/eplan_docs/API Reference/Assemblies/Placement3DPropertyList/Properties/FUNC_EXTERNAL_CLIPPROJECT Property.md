# FUNC_EXTERNAL_CLIPPROJECT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_EXTERNAL_CLIPPROJECT(Int32).html

---

Suppl. field for CLIP PROJECT data # 20090.

Syntax

**C#**



public PropertyValue FUNC_EXTERNAL_CLIPPROJECT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_EXTERNAL_CLIPPROJECT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

This property (max of 1,000, definable using the index) allows CLIP PROJECT data to be stored at functions when importing data from CLIP PROJECT.
