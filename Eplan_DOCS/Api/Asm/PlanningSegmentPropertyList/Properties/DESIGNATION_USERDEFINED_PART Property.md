# DESIGNATION_USERDEFINED_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DESIGNATION_USERDEFINED_PART().html

---

User-defined structure (single component) # 1628.

Syntax

**C#**



public PropertyValue DESIGNATION_USERDEFINED_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_USERDEFINED_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of the user-defined structure that is entered at this planning object. The entire user-defined structure for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
