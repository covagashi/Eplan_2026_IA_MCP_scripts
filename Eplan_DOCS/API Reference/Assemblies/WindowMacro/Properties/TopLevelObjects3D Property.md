# TopLevelObjects3D Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~TopLevelObjects3D.html

---

Returns all Eplan.EplApi.DataModel.Placement3D, with no parent.

Syntax

**C#**



public Placement3D[] TopLevelObjects3D {get;}

public:

property array<Placement3D^>^ TopLevelObjects3D {

   array<Placement3D^>^ get();

}


#### Property Value

[Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)

Remarks

This array contains all 3d functions which didn't had a parent assigned when the macro was created or their parent wasn't added into this macro. If installation space was included then it will be in this array also.
