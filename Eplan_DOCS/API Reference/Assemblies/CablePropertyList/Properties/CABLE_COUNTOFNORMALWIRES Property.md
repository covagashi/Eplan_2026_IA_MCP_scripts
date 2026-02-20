# CABLE_COUNTOFNORMALWIRES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CablePropertyList~CABLE_COUNTOFNORMALWIRES().html

---

Cables: Number of general connections # 35105.

Syntax

**C#**



public PropertyValue CABLE_COUNTOFNORMALWIRES {get; set;}

public:

property PropertyValue^ CABLE_COUNTOFNORMALWIRES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Total number of connections in the cable that are not N, PE or PEN conductors.
