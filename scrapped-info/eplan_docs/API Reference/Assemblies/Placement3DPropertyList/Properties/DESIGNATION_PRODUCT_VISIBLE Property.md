# DESIGNATION_PRODUCT_VISIBLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~DESIGNATION_PRODUCT_VISIBLE().html

---

Product (visible) # 1829.

Syntax

**C#**



public PropertyValue DESIGNATION_PRODUCT_VISIBLE {get; set;}

public:

property PropertyValue^ DESIGNATION_PRODUCT_VISIBLE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the "Product aspect" component of the visible DT. A value is only displayed here if the extended reference identification is activated in the project structure and the product aspect is used for structuring. Blanks or line breaks that are available in the displayed DT are not displayed for this property.
