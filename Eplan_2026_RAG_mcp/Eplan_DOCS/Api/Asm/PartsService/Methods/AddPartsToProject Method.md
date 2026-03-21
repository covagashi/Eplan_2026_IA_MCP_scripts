# AddPartsToProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~AddPartsToProject.html

---

Store parts in the project, and adds project part references.

Syntax

**C#**



public void AddPartsToProject( 

   Project oProject,

   ArrayList lPartsInfo

)

public:

void AddPartsToProject( 

   Project^ oProject,

   ArrayList^ lPartsInfo

)


#### Parameters

*oProject*
:   Project.

*lPartsInfo*
:   List of parts data. The members of this list have the type 'PartInfo'.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while storing parts data. |
| **ApplicationException** | The internal interface for storing parts data in the project could not be created . |
