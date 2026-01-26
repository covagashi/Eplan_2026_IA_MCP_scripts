# GetTemplatesFromDeviceList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~GetTemplatesFromDeviceList.html

---

This method returns an array of DeviceService::TemplatesInfo containing information about function templates associated with specific part numbers existing in the device list of the given project.

Syntax

**C#**



public DeviceService.TemplatesInfo[] GetTemplatesFromDeviceList( 

   Project oProject

)

public:

array<DeviceService.TemplatesInfo^>^ GetTemplatesFromDeviceList( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project from which the device list will be searched.

#### Return Value

An array of DeviceService::TemplatesInfo objects containing information about function templates associated with specific part numbers.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
