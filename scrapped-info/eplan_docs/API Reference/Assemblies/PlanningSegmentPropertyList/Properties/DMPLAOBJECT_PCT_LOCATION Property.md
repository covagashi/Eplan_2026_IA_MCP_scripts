# DMPLAOBJECT_PCT_LOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_PCT_LOCATION().html

---

Activation site # 44044.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PCT_LOCATION {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PCT_LOCATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Activation site from the PCT type. The following values are possible:

0 = On-site

1 = Measuring station

2 = Control room

3 = Measuring station (not visible)

4 = Control room (not visible).
