# Property(SegmentDefinition,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1071.html

---

Functional assignment (single component) # 1328.

Syntax

**C#**



public PropertyValue DESIGNATION_FUNCTIONALASSIGNMENT_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_FUNCTIONALASSIGNMENT_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of the functional assignment that is entered at this planning object. The entire functional assignment for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
