# OpenPageWithNameAndFunctionName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithNameAndFunctionName.html

---

Opens the page which contains a given function. The function is selected in the graphic editor.

Syntax

**C#**



public void OpenPageWithNameAndFunctionName( 

   string strFullLinkFileName,

   string strPageName,

   string strFuncName

)

public:

void OpenPageWithNameAndFunctionName( 

   String^ strFullLinkFileName,

   String^ strPageName,

   String^ strFuncName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*strPageName*
:   Name of the page to open - if empty it will search in whole project.

*strFuncName*
:   Name of a function.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown in case of invalid parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |

Remarks

First found function will be selected. If page name parameter is empty whole project will be searched. This method searches even for non logic functions.
