# ModulePositions Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ModulePositions.html

---

Get all Module positions of the part.

Syntax

**C#**



public MDPartModulePosition[] ModulePositions {get;}

public:

property array<MDPartModulePosition^>^ ModulePositions {

   array<MDPartModulePosition^>^ get();

}


Remarks

The part has to be a Type: Enums.Module to be able to store module positions.
