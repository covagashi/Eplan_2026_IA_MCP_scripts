# CompareProjects(Project,Project,String,Boolean,String,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1449.html

---

Compares a project to a comparison project. Used for property comparison.

Syntax

**C#**



public void CompareProjects( 

   Project oProject,

   Project oRevision,

   string strSchemaName,

   bool bRemoveOldMarkers,

   string strRevisionMarker,

   bool bUseAlternateIdentification,

   bool bCreateDeletedObjectInfo,

   bool bAppendResult

)

public:

void CompareProjects( 

   Project^ oProject,

   Project^ oRevision,

   String^ strSchemaName,

   bool bRemoveOldMarkers,

   String^ strRevisionMarker,

   bool bUseAlternateIdentification,

   bool bCreateDeletedObjectInfo,

   bool bAppendResult

)


#### Parameters

*oProject*
:   Project to compare.

*oRevision*
:   Comparison project to compare to.

*strSchemaName*
:   Name of the scheme for the comparison settings.

*bRemoveOldMarkers*
:   If set to true, old revision markers will be deleted before comparing.

*strRevisionMarker*
:   Text for the revision markers.

*bUseAlternateIdentification*
:   If set to true, an alternative identification for objects is used. P.e. two functions with the same full BMK are compared with each other.

*bCreateDeletedObjectInfo*
:   If set to true, creates a deleted object symbol for all deleted instances.

*bAppendResult*
:   If set to true, already existing comparison results in the project are not deleted.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when comparing projects. |
| **InvalidScheme** | Used scheme name doesn't exist. |

Remarks

Used for property comparison. If an empty string is passed for the scheme name, everything is compared (i.e. devices, connections,...).
