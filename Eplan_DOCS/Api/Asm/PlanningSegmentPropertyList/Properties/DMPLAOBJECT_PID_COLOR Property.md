# DMPLAOBJECT_PID_COLOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_PID_COLOR().html

---

Color for P&I diagram # 44086.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PID_COLOR {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PID_COLOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

In order to recognize in the P&I diagram which containers, PCT loops, pipings etc. are linked with segments in the pre-planning you can color these components and objects in the P&I diagram. With this property you specify the desired color. In addition the settings for the coloring of components and pipings in the P&I diagram must be activated in the project settings for the pre-planning.
