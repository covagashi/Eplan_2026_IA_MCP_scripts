# ResetPositions3D(Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.WindowMacro~ResetPositions3D(Int32).html

---

Resets positions of items of a 3d macro according to one of its objects.

Syntax

**C#**



public void ResetPositions3D( 

   int nIndex

)

public:

void ResetPositions3D( 

   int nIndex

)


#### Parameters

*nIndex*
:   Index of .TopLevelObjects3D from a macro 3d

Remarks

After calling the method, each 3d object is transformed by inverted transformation of .TopLevelObjects3D[nIndex]
