# FUNC_ARTICLE_SPEED_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_SPEED_MAX(Int32).html

---

Rotation speed, max. # 26256.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SPEED_MAX( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SPEED_MAX {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum permitted rotational speed for a tool or a tool holder.
