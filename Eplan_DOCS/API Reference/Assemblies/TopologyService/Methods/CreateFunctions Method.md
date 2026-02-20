# CreateFunctions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TopologyService~CreateFunctions.html

---

Creates topology functions that are connected to structure routing fulcrums.

Syntax

**C#**



public void CreateFunctions( 

   Project pProject

)

public:

void CreateFunctions( 

   Project^ pProject

)


#### Parameters

*pProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) for which functions will be created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.ArgumentException](#) | If any parameter is invalid. |
