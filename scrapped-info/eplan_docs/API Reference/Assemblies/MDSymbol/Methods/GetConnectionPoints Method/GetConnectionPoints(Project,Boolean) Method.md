# GetConnectionPoints(Project,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbol~GetConnectionPoints(Project,Boolean).html

---

Returns an array of connection points defined in the symbol's function definition.

Syntax

**C#**



public Pin[] GetConnectionPoints( 

   Project project,

   out bool bVariableCount

)

public:

array<Pin^>^ GetConnectionPoints( 

   Project^ project,

   [Out] bool bVariableCount

)


#### Parameters

*project*
:   An opened project which is needed to get a function definition library to read the connection points from.

*bVariableCount*
:   An out parameter which indicates whether the count of connection points is specified as variable in the symbol's function definition.
