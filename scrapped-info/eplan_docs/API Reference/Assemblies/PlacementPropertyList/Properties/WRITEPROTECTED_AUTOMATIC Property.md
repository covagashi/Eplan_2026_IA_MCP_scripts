# WRITEPROTECTED_AUTOMATIC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html

---

Change protection (hierarchical) # 3015.

Syntax

**C#**



public PropertyValue WRITEPROTECTED_AUTOMATIC {get; set;}

public:

property PropertyValue^ WRITEPROTECTED_AUTOMATIC {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Shows whether an object (for example a page, function, planning object, hierarchy level in a navigator) is protected itself or is protected by a superior object. This property also exists at other objects that can be protected by a superior object, for example at interruption points or graphical element.
