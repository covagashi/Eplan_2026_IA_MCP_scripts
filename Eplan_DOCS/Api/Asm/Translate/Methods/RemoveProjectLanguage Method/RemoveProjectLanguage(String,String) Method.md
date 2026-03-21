# RemoveProjectLanguage(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~RemoveProjectLanguage(String,String).html

---

Method for removing a project language. It removes the language from the set of displayed languages.

Syntax

**C#**



public void RemoveProjectLanguage( 

   string strProjectName,

   string strLanguage

)

public:

void RemoveProjectLanguage( 

   String^ strProjectName,

   String^ strLanguage

)


#### Parameters

*strProjectName*
:   Full link file name of the project to be processed.

*strLanguage*
:   Shortcut of the language to be removed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project does not exist. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while removing a language. |

Remarks

It is not possible to remove the source language! System message will be generated in this case.
