# TranslateProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateProject.html

---

Translates all texts in the specified project.

Syntax

**C#**



public void TranslateProject( 

   string strProjectName

)

public:

void TranslateProject( 

   String^ strProjectName

)


#### Parameters

*strProjectName*
:   Full link file name of the project to be translated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project does not exist. |
| **ApplicationException** | \Internal interface necessary for translation could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred, while translating the project. |

Remarks

The specified project may be open in EPLAN or not. If the project is not opened from the beginning, it will be opened for the translation process and will be closed subsequently.
