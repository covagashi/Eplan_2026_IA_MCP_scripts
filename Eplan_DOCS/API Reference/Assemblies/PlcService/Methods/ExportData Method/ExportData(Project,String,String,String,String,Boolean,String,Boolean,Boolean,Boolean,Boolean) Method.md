# ExportData(Project,String,String,String,String,Boolean,String,Boolean,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1397.html

---

Exports PLC data using the specified converter.

Syntax

**C#**



public void ExportData( 

   Project oProject,

   string strConfigurationProject,

   string strConverterID,

   string strLanguage,

   string strOutputFileName,

   bool bOverwrite,

   string strFormat,

   bool bExportPortSpecificInterconnection,

   bool bExportAccessories,

   bool bExportDrives,

   bool bExportDeviceSpecificConfValues

)

public:

void ExportData( 

   Project^ oProject,

   String^ strConfigurationProject,

   String^ strConverterID,

   String^ strLanguage,

   String^ strOutputFileName,

   bool bOverwrite,

   String^ strFormat,

   bool bExportPortSpecificInterconnection,

   bool bExportAccessories,

   bool bExportDrives,

   bool bExportDeviceSpecificConfValues

)


#### Parameters

*oProject*
:   Project which the PLC data will be exported from.

*strConfigurationProject*
:   The name of the PLC configuration data set to export. It must be one of the strings returned by the GetPLCConfigurationProjects function.

*strConverterID*
:   ID of the PLC data converter to use. The IDs of the registered PLC converters together with their full names may be obtained by calling the GetAvailableConverters method.

*strLanguage*
:   Language used during the export operation, e.g. de\_DE, en\_EN, etc.

*strOutputFileName*
:   Full file name of the output file. The file name should have correct extension according to the converter used.

*bOverwrite*
:   If the output file already exists, this parameter specifies whether it should be overwritten.

*strFormat*
:   Format of export file. This can be obtained by calling GetAvailableFormats method.

*bExportPortSpecificInterconnection*
:   Export port-specific interconnection.

*bExportAccessories*
:   Export accessories.

*bExportDrives*
:   Export drives.

*bExportDeviceSpecificConfValues*
:   Export devices-specific configuration values.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for exporting PLC data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |

Remarks

Use the GetAvailableConverters method to get the list of registered PLC data converters. Use the GetAvailableFormats method to get the list of available formats. If the given directory in the full file name does not exist, it will be created.
