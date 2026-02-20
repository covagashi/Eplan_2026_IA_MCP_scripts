# CreateRevision Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CreateRevision.html

---

Creates a new logging revision of the source project. If the source project is a completed revision already, it is copied and the path to the revision project is returned (through pPathOfCopiedRevision parameter). Used for change tracking.

Syntax

**C#**



public void CreateRevision( 

   Project sourceProject,

   string strRevisionName,

   string strRevisionComment,

   ref string pPathOfCopiedRevision

)

public:

void CreateRevision( 

   Project^ sourceProject,

   String^ strRevisionName,

   String^ strRevisionComment,

   String^% pPathOfCopiedRevision

)


#### Parameters

*sourceProject*
:   Project to create a revision from.

*strRevisionName*
:   Name of the new revision.

*strRevisionComment*
:   Description of the new revision.

*pPathOfCopiedRevision*
:   Pointer to a string in which the path to the revision project is returned as long as the source project was a completed revision and a new revision has been created. Otherwise the string is set to an empty value. The pointer itself may be NULL.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when creating a revision. |

Remarks

Used for change tracking. This creates a new logging revision. At this point of time all changes of this document are logged and all objects changed are marked with a marker. In GED this is a border around the object. When a project section is active, only the pages/installation spaces of this section are logged.
