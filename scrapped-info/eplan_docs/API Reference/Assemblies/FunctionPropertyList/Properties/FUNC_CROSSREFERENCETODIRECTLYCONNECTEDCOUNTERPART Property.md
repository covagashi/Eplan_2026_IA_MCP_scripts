# FUNC_CROSSREFERENCETODIRECTLYCONNECTEDCOUNTERPART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic256.html

---

Cross-reference to plug counterpiece # 20304.

Syntax

**C#**



public PropertyValue FUNC_CROSSREFERENCETODIRECTLYCONNECTEDCOUNTERPART {get; set;}

public:

property PropertyValue^ FUNC_CROSSREFERENCETODIRECTLYCONNECTEDCOUNTERPART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

A cross-reference to the counterpart is displayed at the plug definition (i.e. the assigned plug definition representing the receptacle / coupling). For a combined representation of male and female pins in one function, no cross-reference is displayed. A cross-reference to the matching pin is displayed at the pins. If male and female pins have the same DT, only the position of the matching pin is displayed. For non-placed direct connections, the cross-reference shows the name and position of the connected counterpart.
