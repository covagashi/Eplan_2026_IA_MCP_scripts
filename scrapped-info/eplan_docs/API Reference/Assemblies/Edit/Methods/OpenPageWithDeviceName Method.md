# OpenPageWithDeviceName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithDeviceName.html

---

Opens the page which contains a given function. The function is selected in the graphic editor.

Syntax

**C#**



public void OpenPageWithDeviceName( 

   string strFullLinkFileName,

   string strDeviceName

)

public:

void OpenPageWithDeviceName( 

   String^ strFullLinkFileName,

   String^ strDeviceName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*strDeviceName*
:   Name of a function.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown in case of invalid parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |

Remarks

The given function can be a main function (motor,...), a device with index (plug, PLC connection,...) or an interruption point. Only the first found function will be selected. The method does not work if a function has graphic or external representation type.
