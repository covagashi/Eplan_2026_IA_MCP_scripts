# DMPLAOBJECT_PRICE_TOTAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~DMPLAOBJECT_PRICE_TOTAL().html

---

Total calculation value # 44019.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PRICE_TOTAL {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PRICE_TOTAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only..

Displays the total of the calculation values that were estimated for the realization of the current segment. To this purpose the calculation values of the current segment (at a planning object) and of all the planning objects lying below this segment are added up. The property is available in reports.
