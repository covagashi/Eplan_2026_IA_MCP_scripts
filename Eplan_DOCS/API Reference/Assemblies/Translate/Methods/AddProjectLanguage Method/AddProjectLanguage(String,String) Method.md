# AddProjectLanguage(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~AddProjectLanguage(String,String).html

---

Method for adding a project language. It adds the language to the set of possible languages.

Syntax

**C#**



public bool AddProjectLanguage( 

   string strFullLinkFileName,

   string strLanguage

)

public:

bool AddProjectLanguage( 

   String^ strFullLinkFileName,

   String^ strLanguage

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project, into which the language will be added.

*strLanguage*
:   Shortcut of the language to be added.

#### Return Value

True, in case of success, or if giving language was added before.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **ApplicationException** | Internal interface necessary for add language could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while adding a language. |
