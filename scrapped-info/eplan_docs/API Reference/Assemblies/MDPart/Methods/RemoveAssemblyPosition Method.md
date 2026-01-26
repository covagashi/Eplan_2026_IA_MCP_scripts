# RemoveAssemblyPosition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~RemoveAssemblyPosition.html

---

Removes the given assembly position from the part.

Syntax

**C#**



public void RemoveAssemblyPosition( 

   MDPartAssemblyPosition assemblyPos

)

public:

void RemoveAssemblyPosition( 

   MDPartAssemblyPosition^ assemblyPos

)


#### Parameters

*assemblyPos*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if `assemblyPos` is `null`. |

Remarks

The part has to be a Type: Enums.Assembly to be able to store asssembly positions.
