# SynchronizeObjectsToNavigators Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~SynchronizeObjectsToNavigators.html

---

Synchronize objects selected in GUI navigators. Groups will not be resolved, each object of a group must be given in parameter.

Syntax

**C#**



public void SynchronizeObjectsToNavigators( 

   StorableObject[] objects

)

public:

void SynchronizeObjectsToNavigators( 

   array<StorableObject^>^ objects

)


#### Parameters

*objects*
:   Storable objects to select.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
