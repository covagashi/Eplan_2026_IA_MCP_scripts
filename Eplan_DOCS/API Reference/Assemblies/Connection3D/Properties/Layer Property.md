# Layer Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Connection3D~Layer.html

---

Gets or sets object's graphical layer.

Syntax

**C#**



public GraphicalLayer Layer {get; set;}

public:

property GraphicalLayer^ Layer {

   GraphicalLayer^ get();

   void set (    GraphicalLayer^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown, while setting if new layer is not a 3D layer. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown, if changing object's layer failed. |
