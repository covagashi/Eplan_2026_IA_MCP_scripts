# FUNC_ARTICLE_CONSTRUCTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CONSTRUCTION(Int32).html

---

Used drilling pattern # 20284.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CONSTRUCTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CONSTRUCTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Shows the drilling patterns (max. 50) in use of a part number assigned to a function.
