# GetAllDeviceListItems Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~GetAllDeviceListItems.html

---

Returns an array of all device list items in the project.

Syntax

**C#**



public DeviceListEntry[] GetAllDeviceListItems( 

   Project oProject

)

public:

array<DeviceListEntry^>^ GetAllDeviceListItems( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project to get the items from.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid argument. |
| **ArgumentNullException** | Is thrown, if some argument was not passed. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an error occurred while getting the device list entries. |
