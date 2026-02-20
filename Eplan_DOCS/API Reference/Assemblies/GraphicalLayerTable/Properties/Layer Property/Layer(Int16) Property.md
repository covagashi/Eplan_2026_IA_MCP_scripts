# Layer(Int16) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Layer(Int16).html

---

Returns one the project's layer as GraphicalLayer object. If specified layer not exist, null is returned.

Syntax

**C#**



public GraphicalLayer Layer( 

   short id

) {get;}

public:

property GraphicalLayer^ Layer {

   GraphicalLayer^ get(short id);

}


#### Parameters

*id*
:   Id of the layer to retrieve
