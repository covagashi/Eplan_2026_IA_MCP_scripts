# RootElements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~RootElements.html

---

List of [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) which will be displayed together with their children.

Syntax

**C#**



public Placement3D[] RootElements {get; set;}

public:

property array<Placement3D^>^ RootElements {

   array<Placement3D^>^ get();

   void set (    array<Placement3D^>^ value);

}


Remarks

Changes are visible after calling [Update](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~Update.html).
