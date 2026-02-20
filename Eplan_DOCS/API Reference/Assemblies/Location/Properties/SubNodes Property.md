# SubNodes Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location~SubNodes.html

---

Gets all child locations in the same hierarchy (e.g. for +A.A.A it may be: +A.A.A.A, +A.A.A.B, +A.A.A.C, or other)

Syntax

**C#**



public Location[] SubNodes {get;}

public:

property array<Location^>^ SubNodes {

   array<Location^>^ get();

}

