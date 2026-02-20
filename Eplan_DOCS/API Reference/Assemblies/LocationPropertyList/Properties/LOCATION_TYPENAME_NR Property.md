# LOCATION_TYPENAME_NR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_TYPENAME_NR().html

---

Identifier block (ID) # 1006.

Syntax

**C#**



public PropertyValue LOCATION_TYPENAME_NR {get; set;}

public:

property PropertyValue^ LOCATION_TYPENAME_NR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

This property is read-only..

Provides (regardless of the language) the identifier block to which the structure identifier belongs, e.g. "Function designation," "Location designation" etc. This property can be used in reports, e.g. in the structure identifier overview.
