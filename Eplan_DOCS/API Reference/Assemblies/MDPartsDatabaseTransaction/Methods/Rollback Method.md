# Rollback Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseTransaction~Rollback.html

---

Rollback the database transaction. The changes are not stored.

Syntax

**C#**



public void Rollback()

public:

void Rollback();


Remarks

Warning: after calling the method, objects from Eplan::EplApi::MasterData namespace has to be get again in order to have up-to-date properties.
