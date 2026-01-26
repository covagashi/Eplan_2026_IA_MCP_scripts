# RemoveProjectLanguages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~RemoveProjectLanguages.html

---

Method for removing a collection of languages from a project.

Syntax

**C#**



public bool RemoveProjectLanguages( 

   Project pProject,

   StringCollection listLanguages

)

public:

bool RemoveProjectLanguages( 

   Project^ pProject,

   StringCollection^ listLanguages

)


#### Parameters

*pProject*
:   Project to be processed.

*listLanguages*
:   String collection containing languages to remove.

#### Return Value

Returns True if successful, False if removing at least one of languages failed.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while removing a language. |
| **ArgumentNullException** | Thrown if null was passed as an argument. |

Remarks

It is not possible to remove the source language! System message will be generated in this case. Method removes not only languages from project pool, but also translations from multilangual strings in a project.
