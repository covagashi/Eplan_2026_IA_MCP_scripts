# FUNC_ARTICLE_ACCURACY_FOR_DYNAMIC_VISCOSITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic143.html

---

Dynamic viscosity: Accuracy # 26363.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACCURACY_FOR_DYNAMIC_VISCOSITY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACCURACY_FOR_DYNAMIC_VISCOSITY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Describes the precision with which a device or system can measure the dynamic viscosity of a liquid. This specification is often expressed as a percentage (%) and indicates how accurate the measurements are compared to the actual value.
