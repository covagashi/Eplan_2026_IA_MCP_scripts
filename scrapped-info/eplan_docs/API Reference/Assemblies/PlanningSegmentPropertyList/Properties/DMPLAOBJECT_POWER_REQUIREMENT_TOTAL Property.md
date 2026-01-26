# DMPLAOBJECT_POWER_REQUIREMENT_TOTAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic857.html

---

Total expenditure software # 44017.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_PROGRAMMINGTIME_TOTAL {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_PROGRAMMINGTIME_TOTAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

It displays the total of the time that was estimated for the programming of the current segment. To this purpose the required times of the current segment (at a planning object) and of all the planning objects lying below this segment are added up. The property is available in reports.
