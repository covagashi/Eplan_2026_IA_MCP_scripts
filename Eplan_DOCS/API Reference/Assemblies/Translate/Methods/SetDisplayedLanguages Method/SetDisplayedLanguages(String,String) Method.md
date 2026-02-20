# SetDisplayedLanguages(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~SetDisplayedLanguages(String,String).html

---

Method for adding a language that will be displayed in the project.

Syntax

**C#**



public bool SetDisplayedLanguages( 

   string strFullLinkFileName,

   string strLanguage

)

public:

bool SetDisplayedLanguages( 

   String^ strFullLinkFileName,

   String^ strLanguage

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, into which the language will be added.

*strLanguage*
:   Shortcut of the language (or languages separated by comma) to be set.

#### Return Value

True, in case of success, or if giving language was added before.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **ApplicationException** | Internal interface necessary for add language could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while adding a language. |
