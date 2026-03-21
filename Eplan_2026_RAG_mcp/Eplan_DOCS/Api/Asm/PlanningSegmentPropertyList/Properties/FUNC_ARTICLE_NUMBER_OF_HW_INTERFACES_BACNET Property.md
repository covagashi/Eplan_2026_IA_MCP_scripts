# FUNC_ARTICLE_NUMBER_OF_HW_INTERFACES_BACNET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic970.html

---

Number of inputs # 26217.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NUMBER_OF_INPUTS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NUMBER_OF_INPUTS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Number of inputs.
