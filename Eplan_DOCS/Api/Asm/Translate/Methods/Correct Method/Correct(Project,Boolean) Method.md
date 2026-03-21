# Correct(Project,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~Correct(Project,Boolean).html

---

Correct translations in project.

Syntax

**C#**



public void Correct( 

   Project oProject,

   bool bConvertAlreadyTranslatedTexts

)

public:

void Correct( 

   Project^ oProject,

   bool bConvertAlreadyTranslatedTexts

)


#### Parameters

*oProject*
:   Project from which texts will be corrected.

*bConvertAlreadyTranslatedTexts*
:   When set to `true` already converted texts are also translated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown when project is invalid. |
| **ArgumentNullException** | Thrown when project is `null`. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an error occurred during correction. |

Remarks

Method coresponds to Project->Translation->Extent in GUI and uses project settings to determine which texts should be corrected.
