# FUNC_ARTICLEREF_PARTSLISTGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLEREF_PARTSLISTGROUP(Int32).html

---

Bill of materials group # 20924.

Syntax

**C#**



public PropertyValue FUNC_ARTICLEREF_PARTSLISTGROUP( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLEREF_PARTSLISTGROUP {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

You can use this property to group the parts data of components, serial machines, etc. and to make these groups visible in the bill of materials navigator. The property can be used for filtering in the bill of materials and 3D mounting layout navigator and is available in the reports for the bill of materials and for editing in tables.
