# ExportDeviceList(Project,String,Format) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ExportDeviceList(Project,String,Format).html

---

This function exports the device list of a given project. It is used for exporting devices from the planning list (but neither all devices from the project nor all from the bill of materials).

Syntax

**C#**



public void ExportDeviceList( 

   Project oProject,

   string strExportFilePath,

   DeviceService.Format fileFormat

)

public:

void ExportDeviceList( 

   Project^ oProject,

   String^ strExportFilePath,

   DeviceService.Format fileFormat

)


#### Parameters

*oProject*
:   Project from which the device list will be exported.

*strExportFilePath*
:   Full file name of the device list file to export.

*fileFormat*
:   Format of the export file\: By default the following file formats are available\: XML or CSV. The enum Format defines the available values. If an invalid format is set, the file is exported as XML.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for exporting a device list could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export of a device list. Please refer to the exception message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidConverter](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidConverter.html) | Thrown when given parameter  `fileFormat`  isn't valid converter or such conversion dosesn't exist at all. |
