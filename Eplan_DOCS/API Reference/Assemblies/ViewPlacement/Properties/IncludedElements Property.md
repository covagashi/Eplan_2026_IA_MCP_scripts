# IncludedElements Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~IncludedElements.html

---

List of [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) which will be displayed.

Syntax

**C#**



public Placement3D[] IncludedElements {get; set;}

public:

property array<Placement3D^>^ IncludedElements {

   array<Placement3D^>^ get();

   void set (    array<Placement3D^>^ value);

}


Remarks

Objects which don't contain mesh like Cabinet will not be displayed. To display elements of Cabinet it is necessary to include their children.

Changes are visible after calling [Update](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~Update.html).
