# DESIGNATION_PLANT_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DESIGNATION_PLANT_PART().html

---

Function designation (single component) # 1128.

Syntax

**C#**



public PropertyValue DESIGNATION_PLANT_PART {get; set;}

public:

property PropertyValue^ DESIGNATION_PLANT_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Part of function designation that is entered at this planning object. The entire function designation for a planning object consists in this case of the own individual part and all the parts of the superior structure segments and planning objects.
