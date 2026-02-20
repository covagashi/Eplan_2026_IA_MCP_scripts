# CreateTransient(Project,String,List<Placement3D>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic477.html

---

Creates transient InstallationSpace object and sets a name.

Syntax

**C#**



public static InstallationSpace CreateTransient( 

   Project oProject,

   string strName,

   List<Placement3D> listOfAdditionalObjects

)

public:

static InstallationSpace^ CreateTransient( 

   Project^ oProject,

   String^ strName,

   List<Placement3D^>^ listOfAdditionalObjects

)


#### Parameters

*oProject*
:   Project to which this object will be assign. Can't be null.

*strName*
:   Name which is set to InstallationSpace after creation. Can't be null or have zero length.

*listOfAdditionalObjects*
:   list, that will be filled by additional created objects. may be null

#### Return Value

The created Installation space.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the InstallationSpace cannot be created. |
