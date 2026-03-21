# DeleteDeviceListItem Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~DeleteDeviceListItem.html

---

Removes the entry from the project's device list.

Syntax

**C#**



public void DeleteDeviceListItem( 

   DeviceListEntry oEntry

)

public:

void DeleteDeviceListItem( 

   DeviceListEntry^ oEntry

)


#### Parameters

*oEntry*
:   The entry to remove.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid arguments. |
| **ArgumentNullException** | Is thrown, if some argument was not passed. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an error occurred while removing a device list entry. |
