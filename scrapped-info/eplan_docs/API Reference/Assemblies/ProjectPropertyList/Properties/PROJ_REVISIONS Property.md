# PROJ_REVISIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_REVISIONS(Int32).html

---

Revisions # 10150.

Syntax

**C#**



public PropertyValue PROJ_REVISIONS( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_REVISIONS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Revision designations, max 1,000 allowed.
