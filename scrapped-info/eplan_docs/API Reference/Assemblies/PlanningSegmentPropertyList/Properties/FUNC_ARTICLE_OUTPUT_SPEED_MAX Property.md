# FUNC_ARTICLE_OUTPUT_SPEED_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic977.html

---

Output speed, min. # 26186.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_OUTPUT_SPEED_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_OUTPUT_SPEED_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum rotation speed at the output shaft in the working range.
