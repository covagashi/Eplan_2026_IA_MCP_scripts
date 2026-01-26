# TranslatePage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslatePage.html

---

Translates all texts of a page in the specified project.

Syntax

**C#**



public void TranslatePage( 

   string strProjectName,

   string strPage

)

public:

void TranslatePage( 

   String^ strProjectName,

   String^ strPage

)


#### Parameters

*strProjectName*
:   Full link file name of the project, which contains the page.

*strPage*
:   Full name of the page to be translated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project does not exist. |
| **ApplicationException** | \Internal interface necessary for translation could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred, while translating the page. |

Remarks

The specified project may be open in EPLAN or not. If the project is not opened from the beginning, it will be opened for the translation process and will be closed subsequently.
