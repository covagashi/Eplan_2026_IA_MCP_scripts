# Layer(Int16) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.TransientLayerTable~Layer(Int16).html

---

Returns one the project's layer as TransientLayer object. If specified layer not exist, null is returned.

Syntax

**C#**



public TransientLayer Layer( 

   short id

) {get;}

public:

property TransientLayer^ Layer {

   TransientLayer^ get(short id);

}


#### Parameters

*id*
:   Id of the layer to retrieve
