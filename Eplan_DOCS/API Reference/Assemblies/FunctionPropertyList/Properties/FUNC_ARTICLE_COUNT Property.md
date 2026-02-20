# FUNC_ARTICLE_COUNT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_COUNT(Int32).html

---

Number of units / quantity # 20102.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_COUNT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_COUNT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Shows the (max. 50) number of units of the part number assigned to a function.
