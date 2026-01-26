# DESIGNATION_FULLSUBPLANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~DESIGNATION_FULLSUBPLANT().html

---

Function designation (sub-identifier, complete) # 1121.

Syntax

**C#**



public PropertyValue DESIGNATION_FULLSUBPLANT {get; set;}

public:

property PropertyValue^ DESIGNATION_FULLSUBPLANT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For a function designation provides all the sub-identifiers, for example "UA1.UA2" at a complete function designation "A.UA1.UA2".
