# FUNC_GEDNAMEWITHCONNECTIONDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_GEDNAMEWITHCONNECTIONDESIGNATION().html

---

Connection point designation (with displayed DT) # 20036.

Syntax

**C#**



public PropertyValue FUNC_GEDNAMEWITHCONNECTIONDESIGNATION {get; set;}

public:

property PropertyValue^ FUNC_GEDNAMEWITHCONNECTIONDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the entered designation for connection points. This consists of the combination of a "normal" DT and connection point designation for "normal" connection points, separated by a colon (or a character that can be freely defined).
