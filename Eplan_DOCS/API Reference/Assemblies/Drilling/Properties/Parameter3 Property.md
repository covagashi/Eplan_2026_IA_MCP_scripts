# Parameter3 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Drilling~Parameter3.html

---

Parameter3.

Syntax

**C#**



public double Parameter3 {get; set;}

public:

property double Parameter3 {

   double get();

   void set (    double value);

}


Remarks

Usage of this parameter is dependant on function definition id and ItemType :

- id: `3 (Rectangles)` ItemType: `Eplan::EplApi::Base::Enums::ItemType::DrillingRectRounded` - diameter
- id: `3 (Rectangles)` ItemType: `Eplan::EplApi::Base::Enums::ItemType::DrillingRectChamfer` - chamfer length

In other cases this parameter is not used.
