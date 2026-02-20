# CreateReportsFromTemplates Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Reports~CreateReportsFromTemplates.html

---

Creates reports from templates of given document type.

Syntax

**C#**



public void CreateReportsFromTemplates( 

   Project oProject,

   ICollection<DocumentTypeManager.DocumentType> colDocTypes

)

public:

void CreateReportsFromTemplates( 

   Project^ oProject,

   ICollection<DocumentTypeManager.DocumentType>^ colDocTypes

)


#### Parameters

*oProject*
:   Project in which reports will be created.

*colDocTypes*
:   Collection report template types which from which reports will be generated.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any of parameters is null. |
| [System.ArgumentException](#) | If any of parameters is invlaid. |
| [System.ApplicationException](#) | Failed to create reports. Please refer to the error message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An internal error occurred during creating embedded report Please refer to the error message. |
