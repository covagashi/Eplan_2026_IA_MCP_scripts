# DESIGNATION_PRODUCT_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DESIGNATION_PRODUCT_PART().html

---

Product aspect (single component) # 1828.

Syntax

**C#**



public PropertyValue DESIGNATION_PRODUCT_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_PRODUCT_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of the product aspect that is entered at this planning object. The entire product aspect for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
