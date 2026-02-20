# Create(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace~Create(Project,String).html

---

Creates InstallationSpace object and sets a name.

Syntax

**C#**



public void Create( 

   Project oProject,

   string strName

)

public:

void Create( 

   Project^ oProject,

   String^ strName

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strName*
:   Name which is set to InstallationSpace after creation. Can't be null or have zero length.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the InstallationSpace cannot be created. |
