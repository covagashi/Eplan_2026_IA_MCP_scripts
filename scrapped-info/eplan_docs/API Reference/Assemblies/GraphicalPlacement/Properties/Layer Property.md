# Layer Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~Layer.html

---

Gets or sets object's graphical layer. If object is not assigned to a project (Project is null), null is returned

Syntax

**C#**



public virtual GraphicalLayer Layer {get; set;}

public:

virtual property GraphicalLayer^ Layer {

   GraphicalLayer^ get();

   void set (    GraphicalLayer^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown, if changing object's layer failed. |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown if layer passed as parameter is not valid (property **Eplan::EplApi::DataModel::Graphics::GraphicalLayer:** returns false). |
