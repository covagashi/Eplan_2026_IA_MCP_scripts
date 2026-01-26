# OpenInstallationSpaceWithDeviceName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit3D~OpenInstallationSpaceWithDeviceName.html

---

Opens the installation space which contains a given function. The function is selected in the graphic editor.

Syntax

**C#**



public void OpenInstallationSpaceWithDeviceName( 

   string strFullLinkFileName,

   string strDeviceName

)

public:

void OpenInstallationSpaceWithDeviceName( 

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
| **ArgumentException** | Is thrown in case of invalid \parameters. |
| **ApplicationException** | The graphics editor interface could not be created. |

Remarks

The given function can be a main function (motor,...), a device with index (plug, PLC connection,...) or an interruption point. Only the first found function will be selected.
