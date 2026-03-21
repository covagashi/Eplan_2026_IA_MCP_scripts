# FUNC_CABLE_DEVTAGINCLUDESSOURCEORDESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic619.html

---

Cable name includes source / target # 20069.

Syntax

**C#**



public PropertyValue FUNC_CABLE_DEVTAGINCLUDESSOURCEORDESTINATION {get; set;}

public:

property PropertyValue^ FUNC_CABLE_DEVTAGINCLUDESSOURCEORDESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is no longer in use and only taken into consideration in old projects. Specifies whether the cable name contains source and / or target. In this case the DT is handled differently in the DT calculation.
