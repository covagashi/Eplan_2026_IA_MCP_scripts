# DeleteDeviceList(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~DeleteDeviceList(Project).html

---

This function deletes the device list in the given project.

Syntax

**C#**



public void DeleteDeviceList( 

   Project oProject

)

public:

void DeleteDeviceList( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project in which the device list will be deleted.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | null was passed to a parameter. |
| **ApplicationException** | The internal interface for deleting device lists could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while deleting the device list. Please refer to the exception message. |
