# CreateTransient Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.HyperLink~CreateTransient.html

---

Creates transient and not placed HyperLink object.

Syntax

**C#**



public override void CreateTransient( 

   Project oProject

)

public:

void CreateTransient( 

   Project^ oProject

) override


#### Parameters

*oProject*
:   [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html) the HyperLink will be attached to.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `oProject` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the HyperLink cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the HyperLink has already been created. |
