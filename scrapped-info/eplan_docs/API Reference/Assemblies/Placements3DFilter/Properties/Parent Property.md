# Parent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~Parent.html

---

Sets the [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) for which all children will be found.

Syntax

**C#**



public Placement3D Parent {get; set;}

public:

property Placement3D^ Parent {

   Placement3D^ get();

   void set (    Placement3D^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
