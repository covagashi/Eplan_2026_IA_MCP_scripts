# FUNC_ARTICLE_CLOSING_PRESSURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CLOSING_PRESSURE(Int32).html

---

Closing pressure # 26552.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CLOSING_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CLOSING_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Pressure to close an item under defined conditions.
