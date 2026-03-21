# InstallationSpace Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~InstallationSpace.html

---

Sets the [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) that [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html)s matching the filter must be placed in.

Syntax

**C#**



public InstallationSpace InstallationSpace {get; set;}

public:

property InstallationSpace^ InstallationSpace {

   InstallationSpace^ get();

   void set (    InstallationSpace^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
