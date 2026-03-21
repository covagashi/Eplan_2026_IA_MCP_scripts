# FUNC_ARTICLE_SPEED_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_SPEED_MIN(Int32).html

---

Rotation speed, min. # 26258.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SPEED_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SPEED_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum possible rotation speed at which a motor can be operated continuously at the thermally permissible rated operating point.
