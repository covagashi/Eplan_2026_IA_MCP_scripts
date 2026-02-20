# WriteBackFunctionData Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MergeDataService~WriteBackFunctionData.html

---

Writes back the data of merged functions to whose corresponding functions

Syntax

**C#**



public static void WriteBackFunctionData( 

   MergedFunction[] arrMergedFunctions

)

public:

static void WriteBackFunctionData( 

   array<MergedFunction^>^ arrMergedFunctions

)


#### Parameters

*arrMergedFunctions*
:   Merged functions to write back data.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Method failed. |
| [System.ArgumentException](#) | Thrown when the objects in the parameter belong to more than one project. |

Remarks

The objects in the parameter may only belong to one project.
