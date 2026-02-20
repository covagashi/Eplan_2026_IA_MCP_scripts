# DESIGNATION_FULLSUBLOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~DESIGNATION_FULLSUBLOCATION().html

---

Location designation (sub-identifier, complete) # 1221.

Syntax

**C#**



public PropertyValue DESIGNATION_FULLSUBLOCATION {get; set;}

public:

property PropertyValue^ DESIGNATION_FULLSUBLOCATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides all the sub-identifiers for a location designation, e.g. "UO1.UO2" at a complete location designation "O.UO1.UO2".
