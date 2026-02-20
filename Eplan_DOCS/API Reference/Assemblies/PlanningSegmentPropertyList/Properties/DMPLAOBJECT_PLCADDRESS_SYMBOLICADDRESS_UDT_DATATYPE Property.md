# DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT_DATATYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic856.html

---

Total power consumption # 44011.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_POWER_REQUIREMENT_TOTAL {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_POWER_REQUIREMENT_TOTAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Displays the total of the required power consumption that was estimated for the realization of the current segment. To this purpose the required power consumption of the current segment (at a planning object) and of all the planning objects lying below this segment are added up. The property is available in reports.
