# Layer Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Layer.html

---

Returns the [Eplan.EplApi.DataModel.Graphics.GraphicalLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) of the Placement3D.

Syntax

**C#**



public GraphicalLayer Layer {get; set;}

public:

property GraphicalLayer^ Layer {

   GraphicalLayer^ get();

   void set (    GraphicalLayer^ value);

}


#### Property Value

Placement3D's [Eplan.EplApi.DataModel.Graphics.GraphicalLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) or NULL if Placement3D doesn't have FunctionDefinition.
