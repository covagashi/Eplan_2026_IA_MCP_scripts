# MACROBOX_REPRESENTATION_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBoxPropertyList~MACROBOX_REPRESENTATION_TYPE().html

---

Macro: Representation type # 23007.

Syntax

**C#**



public PropertyValue MACROBOX_REPRESENTATION_TYPE {get; set;}

public:

property PropertyValue^ MACROBOX_REPRESENTATION_TYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Representation type of macro. Possible values are:

1 = Multi-line

2 = Single-line

3 = Pair cross-reference

4 = Overview

5 = Graphic

6 = Panel layout

7 = P&I diagram

8 = Multi-line Fluid power

9 = Topology

10 = 3D mounting layout

11 = Functional

12 = Pre-planning.
