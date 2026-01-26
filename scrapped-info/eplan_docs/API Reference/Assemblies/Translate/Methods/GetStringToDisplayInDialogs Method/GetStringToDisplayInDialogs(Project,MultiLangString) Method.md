# GetStringToDisplayInDialogs(Project,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~GetStringToDisplayInDialogs(Project,MultiLangString).html

---

Get string displayed in project dialogs.

Syntax

**C#**



public string GetStringToDisplayInDialogs( 

   Project oProject,

   MultiLangString oMLS

)

public:

String^ GetStringToDisplayInDialogs( 

   Project^ oProject,

   MultiLangString^ oMLS

)


#### Parameters

*oProject*
:   Project from which settings will be read.

*oMLS*
:   String in multiple languages

#### Return Value

String displayed in project dialogs.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if any parameter is invalid. |

Remarks

Displayed language name is choosen from source language, GUI language, alternative language or first of translation languages.
