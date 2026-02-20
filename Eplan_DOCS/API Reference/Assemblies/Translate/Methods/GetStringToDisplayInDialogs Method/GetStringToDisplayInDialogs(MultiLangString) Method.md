# GetStringToDisplayInDialogs(MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~GetStringToDisplayInDialogs(MultiLangString).html

---

Get string displayed in project-independent dialogs (like parts management).

Syntax

**C#**



public string GetStringToDisplayInDialogs( 

   MultiLangString oMLS

)

public:

String^ GetStringToDisplayInDialogs( 

   MultiLangString^ oMLS

)


#### Parameters

*oMLS*
:   String in multiple languages

#### Return Value

String displayed in project-independent dialogs (like parts management)

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Throw if any parameter is invalid. |

Remarks

Displayed language name is choosen from source language, GUI language or alternative language.
