# GetConnectionPoints(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~GetConnectionPoints(Project).html

---

Returns an array of connection points defined in the symbol's function definition.

Syntax

**C#**



public Pin[] GetConnectionPoints( 

   Project project

)

public:

array<Pin^>^ GetConnectionPoints( 

   Project^ project

)


#### Parameters

*project*
:   An opened project which is needed to get a function definition library to read the connection points from.
