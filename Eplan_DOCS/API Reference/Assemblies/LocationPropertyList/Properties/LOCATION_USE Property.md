# LOCATION_USE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_USE().html

---

Usage count # 1005.

Syntax

**C#**



public PropertyValue LOCATION_USE {get; set;}

public:

property PropertyValue^ LOCATION_USE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Specifies how often a structure identifier is used in the project ("?" = not updated, \* = not used, but a sub-identifier exists).
