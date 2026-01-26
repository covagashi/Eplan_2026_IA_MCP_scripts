# LOCATION_TYPENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_TYPENAME().html

---

Identifier block # 1004.

Syntax

**C#**



public PropertyValue LOCATION_TYPENAME {get; set;}

public:

property PropertyValue^ LOCATION_TYPENAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the identifier block to which the structure identifier belongs, e.g. "Function designation," "Location designation" etc. The property can be used in forms for the structure identifier overview.
