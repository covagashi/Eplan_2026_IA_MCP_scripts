# CreateDeviceListItem(Project,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~CreateDeviceListItem(Project,String).html

---

Create a new device list entry.

Syntax

**C#**



public DeviceListEntry CreateDeviceListItem( 

   Project oProject,

   string strPartNumber

)

public:

DeviceListEntry^ CreateDeviceListItem( 

   Project^ oProject,

   String^ strPartNumber

)


#### Parameters

*oProject*
:   Project in which the new device list entry will be created.

*strPartNumber*
:   Part number.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Is thrown in case of invalid arguments. |
| **ArgumentNullException** | Is thrown, if some argument was not passed. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an error occurred while creating a device list entry. |
