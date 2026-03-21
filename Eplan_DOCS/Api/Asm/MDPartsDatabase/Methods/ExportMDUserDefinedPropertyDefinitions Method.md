# ExportMDUserDefinedPropertyDefinitions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportMDUserDefinedPropertyDefinitions.html

---

Exports parts user defined properties.

Syntax

**C#**



public bool ExportMDUserDefinedPropertyDefinitions( 

   string strExportFilePath

)

public:

bool ExportMDUserDefinedPropertyDefinitions( 

   String^ strExportFilePath

)


#### Parameters

*strExportFilePath*
:   Full file name of target file. Can't be `null` or `empty`.

#### Return Value

Returns `true` if export is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null was set to `strExportFilePath` parameter. |
| [System.ArgumentException](#) | Thrown when `strExportFilePath` is `empty`. |
