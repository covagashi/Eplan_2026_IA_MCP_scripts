# DeleteDeviceList(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~DeleteDeviceList(String).html

---

This function deletes the device list in the given project.

Syntax

**C#**



public void DeleteDeviceList( 

   string strFullLinkFileName

)

public:

void DeleteDeviceList( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project in which the device list will be deleted.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | null was passed to a parameter. |
| **ApplicationException** | The internal interface for deleting device lists could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while deleting the device list. Please refer to the exception message. |
