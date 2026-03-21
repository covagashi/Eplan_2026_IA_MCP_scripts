# FUNC_ARTICLE_OUTPUT_SPEED_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_OUTPUT_SPEED_MAX(Int32).html

---

Output speed, max. # 26184.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_OUTPUT_SPEED_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_OUTPUT_SPEED_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum rotation speed at the output shaft.
