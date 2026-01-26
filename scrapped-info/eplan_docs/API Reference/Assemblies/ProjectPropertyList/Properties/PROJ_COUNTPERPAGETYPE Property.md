# PROJ_COUNTPERPAGETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_COUNTPERPAGETYPE(Int32).html

---

Number of pages per page type # 10200.

Syntax

**C#**



public PropertyValue PROJ_COUNTPERPAGETYPE( 

   int index

) {get; set;}

public:

property PropertyValue^ PROJ_COUNTPERPAGETYPE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Provides the number of pages for each page type in the project. The page type is specified via the index (in the help system in the "Page types" section).
