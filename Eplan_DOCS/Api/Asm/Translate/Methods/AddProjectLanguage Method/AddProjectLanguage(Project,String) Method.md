# AddProjectLanguage(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~AddProjectLanguage(Project,String).html

---

Method for adding a project language. It adds the language to the set of possible languages.

Syntax

**C#**



public bool AddProjectLanguage( 

   Project pProject,

   string strLanguage

)

public:

bool AddProjectLanguage( 

   Project^ pProject,

   String^ strLanguage

)


#### Parameters

*pProject*
:   Project to be processed.

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
