# ImportData(Project,String,ImportMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.HarnessService~ImportData(Project,String,ImportMode).html

---

Imports Harness data from a file.

Syntax

**C#**



public StorableObject[] ImportData( 

   Project oProject,

   string strFileName,

   HarnessService.ImportMode nImportMode

)

public:

array<StorableObject^>^ ImportData( 

   Project^ oProject,

   String^ strFileName,

   HarnessService.ImportMode nImportMode

)


#### Parameters

*oProject*
:   Project into which the Harness data will be imported.

*strFileName*
:   Full file name of the file to import.

*nImportMode*
:   Mode for the import.

#### Return Value

An array of created or modified StorableObjects.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for importing Harness data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. |

Example

Following example shows how to use the method:

**C#**

```
StorableObject[] arrObjects = new HarnessService().ImportData(m_oTestProject, strDestinationFilePath, HarnessService.ImportMode.Create | HarnessService.ImportMode.Change);

```
