# FUNC_ARTICLE_CURRENT_CONSUMPTION_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CURRENT_CONSUMPTION_MAX(Int32).html

---

Current consumption, max. # 26598.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CURRENT_CONSUMPTION_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CURRENT_CONSUMPTION_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The maximum electric current in amperes (A) that a device or component can draw from the mains during operation.
