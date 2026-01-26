# FUNC_TYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~FUNC_TYPE().html

---

Representation type # 20121.

Syntax

**C#**



public PropertyValue FUNC_TYPE {get; set;}

public:

property PropertyValue^ FUNC_TYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Type of placement of a function (normally contains the page type where the function has been placed). Possible values are:

1 = Multi-line

3 = Overview

-2 = Pair cross-reference

2 = Single-line

38 = P&I diagram

43 = Topology

8 = Panel layout

-6 = Detailed panel layout

-8 = 3D mounting layout

-12 = Functional

-3 = External

7 = Graphic.
