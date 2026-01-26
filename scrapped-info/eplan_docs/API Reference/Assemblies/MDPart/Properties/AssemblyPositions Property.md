# AssemblyPositions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AssemblyPositions.html

---

Get all Assembly positions of the part.

Syntax

**C#**



public MDPartAssemblyPosition[] AssemblyPositions {get;}

public:

property array<MDPartAssemblyPosition^>^ AssemblyPositions {

   array<MDPartAssemblyPosition^>^ get();

}


Remarks

The part has to be a Type: Enums.Assembly to be able to store asssembly positions.
