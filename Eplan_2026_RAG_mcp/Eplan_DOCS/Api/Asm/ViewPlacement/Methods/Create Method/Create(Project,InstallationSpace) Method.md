# Create(Project,InstallationSpace) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~Create(Project,InstallationSpace).html

---

Creates not placed ViewPlacement object.

Syntax

**C#**



public void Create( 

   Project oProject,

   InstallationSpace pInstallationSpace

)

public:

void Create( 

   Project^ oProject,

   InstallationSpace^ pInstallationSpace

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*pInstallationSpace*
:   [Eplan.EplApi.DataModel.E3D.InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) for this ViewPlacement.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the ViewPlacement cannot be created. |

Remarks

If strArticleVariant null or have zero length default variant "1" is used.
