# ReadProjectInfo(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ReadProjectInfo(String,String).html

---

Loads the ProjectInfo.xml file. and sets project properties accordingly.

Syntax

**C#**



public void ReadProjectInfo( 

   string strFullLinkFileName,

   string strPrjInfoXml

)

public:

void ReadProjectInfo( 

   String^ strFullLinkFileName,

   String^ strPrjInfoXml

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project for which the file will be loaded.

*strPrjInfoXml*
:   Full file name of the ProjectInfo.xml file to be loaded.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Thrown, if the \internal interface of the project management module could no be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |

Remarks

The specified project may be open or not. If the project was not open, it will be opened for loadig the XML file and will be closed subsequently.
