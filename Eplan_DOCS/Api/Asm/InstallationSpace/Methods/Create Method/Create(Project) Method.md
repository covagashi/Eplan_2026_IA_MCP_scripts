# Create(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace~Create(Project).html

---

Creates InstallationSpace object.

Syntax

**C#**



public void Create( 

   Project oProject

)

public:

void Create( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the InstallationSpace cannot be created. |
