# PublishProjectForSmartProduction Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~PublishProjectForSmartProduction.html

---

Publishes a project

Syntax

**C#**



public void PublishProjectForSmartProduction( 

   Project oProject,

   string strFileName,

   string strFolderPath,

   string strScheme

)

public:

void PublishProjectForSmartProduction( 

   Project^ oProject,

   String^ strFileName,

   String^ strFolderPath,

   String^ strScheme

)


#### Parameters

*oProject*
:   Project which will be published for EPLAN Smart Production.

*strFileName*
:   Filename with extension

*strFolderPath*
:   Folder path

*strScheme*
:   Name of the export scheme

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Thrown if the \internal action could no be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
