# Definition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Definition.html

---

Returns an object that provides information about the property and its definition.  
The information includes: name of the property, it's data type, whether it is indexed or not, whether it is read-only, upper/lower bounds of values for numerical properties.

Syntax

**C#**



public MDPropertyDefinition Definition {get;}

public:

property MDPropertyDefinition^ Definition {

   MDPropertyDefinition^ get();

}

