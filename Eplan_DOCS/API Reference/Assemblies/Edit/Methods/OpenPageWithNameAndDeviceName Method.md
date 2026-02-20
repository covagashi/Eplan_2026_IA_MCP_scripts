# OpenPageWithNameAndDeviceName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithNameAndDeviceName.html

---

Opens the page with the name passed to strPageName and select the function whose name passed to strDeviceName. The function is selected in the graphic editor. If no function with name strDeviceName was found on the page, so no element will be selected. But the page will be still opened.

Syntax

**C#**



public void OpenPageWithNameAndDeviceName( 

   string strFullLinkFileName,

   string strPageName,

   string strDeviceName

)

public:

void OpenPageWithNameAndDeviceName( 

   String^ strFullLinkFileName,

   String^ strPageName,

   String^ strDeviceName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*strPageName*


*strDeviceName*
:   Name of a function.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown in case of invalid parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |

Remarks

The given function can be a main function (motor,...), a device with index (plug, PLC connection,...) or an interruption point. On a given page only the first found function will be selected, if one found. The method does not work if a function has graphic or external representation type.
