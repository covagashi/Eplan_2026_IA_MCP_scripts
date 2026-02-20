# RemoveProjectLanguage(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~RemoveProjectLanguage(Project,String).html

---

Method for removing a project language. It removes the language from the set of displayed languages.

Syntax

**C#**



public bool RemoveProjectLanguage( 

   Project pProject,

   string strLanguage

)

public:

bool RemoveProjectLanguage( 

   Project^ pProject,

   String^ strLanguage

)


#### Parameters

*pProject*
:   Project to be processed.

*strLanguage*
:   Shortcut of the language to be removed.

#### Return Value

Returns True if successful.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while removing a language. |
| **ArgumentNullException** | Thrown if null was passed as an argument. |

Remarks

It is not possible to remove the source language! System message will be generated in this case. Method removes not only language from project pool, but also translations from multilangual strings in a project.
