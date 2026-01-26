# FUNC_ARTICLE_VISCOSITY_CLASS_ACCORDING_TO_DIN_51519 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic457.html

---

Viscosity class (acc. to DIN 51519) # 26632.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_VISCOSITY_CLASS_ACCORDING_TO_DIN_51519( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_VISCOSITY_CLASS_ACCORDING_TO_DIN_51519 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification which minimum viscosity and which maximum viscosity the respective hydraulic oil has at 40 °C.
