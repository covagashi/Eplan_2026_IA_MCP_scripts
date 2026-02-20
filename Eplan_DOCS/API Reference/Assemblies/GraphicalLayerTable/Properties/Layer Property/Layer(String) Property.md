# Layer(String) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Layer(String).html

---

Returns one the project's layer as GraphicalLayer object. If specified layer not exist, null is returned.

Syntax

**C#**



public GraphicalLayer Layer( 

   string name

) {get;}

public:

property GraphicalLayer^ Layer {

   GraphicalLayer^ get(String^ name);

}


#### Parameters

*name*
:   Name of the layer to retrieve
