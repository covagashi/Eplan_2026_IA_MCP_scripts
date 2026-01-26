# Parameter1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~Parameter1.html

---

Parameter1.

Syntax

**C#**



public double Parameter1 {get; set;}

public:

property double Parameter1 {

   double get();

   void set (    double value);

}


Remarks

Usage of this parameter is different for each function definition id.

- id: `1 (Round)` - diameter
- id: `2 (Tap hole)` - diameter
- id: `3 (All Rectangles)` - height
- id: `4 (Slot)` - height
- id: `5 (Hexagon)` - edge length
- id: `6 (Octagon)` - edge length

In other cases this parameter is not used.
