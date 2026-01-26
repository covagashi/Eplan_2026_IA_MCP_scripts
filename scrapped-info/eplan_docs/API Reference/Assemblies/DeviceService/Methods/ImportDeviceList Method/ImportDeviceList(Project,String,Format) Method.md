# ImportDeviceList(Project,String,Format) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.DeviceService~ImportDeviceList(Project,String,Format).html

---

This function imports a device list into a given project.

Syntax

**C#**



public void ImportDeviceList( 

   Project oProject,

   string strImportFilePath,

   DeviceService.Format fileFormat

)

public:

void ImportDeviceList( 

   Project^ oProject,

   String^ strImportFilePath,

   DeviceService.Format fileFormat

)


#### Parameters

*oProject*
:   Project into which the device list will be imported.

*strImportFilePath*
:   Full file name of the device list file to import.

*fileFormat*
:   Format of the import file\: By default the following file formats are available\: XML or CSV. The enum Format defines the available values. If an invalid format is set, the file is expected to be XML.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | The internal interface for importing a device list could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import of a device list. Please refer to the exception message. |
| [Eplan.EplApi.HEServices.Exceptions.InvalidConverter](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Exceptions.InvalidConverter.html) | Thrown when given parameter  `fileFormat`  isn't valid converter or such conversion dosesn't exist at all. |
