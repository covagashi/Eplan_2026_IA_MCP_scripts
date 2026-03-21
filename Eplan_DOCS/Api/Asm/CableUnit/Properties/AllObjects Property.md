# AllObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.CableUnit~AllObjects.html

---

Returns an array of StorableObjects which contains the same harness name in property HARNESS\_NAME and additionally all connections connected to the connectors marked with harness name.

Syntax

**C#**



public StorableObject[] AllObjects {get;}

public:

property array<StorableObject^>^ AllObjects {

   array<StorableObject^>^ get();

}

