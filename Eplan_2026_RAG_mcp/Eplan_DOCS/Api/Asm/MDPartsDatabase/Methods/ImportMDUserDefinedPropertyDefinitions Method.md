# ImportMDUserDefinedPropertyDefinitions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ImportMDUserDefinedPropertyDefinitions.html

---

Imports parts user defined properties.

Syntax

**C#**



public bool ImportMDUserDefinedPropertyDefinitions( 

   string strImportFilePath

)

public:

bool ImportMDUserDefinedPropertyDefinitions( 

   String^ strImportFilePath

)


#### Parameters

*strImportFilePath*
:   Full file name of source file. Can't be `null` or `empty`.

#### Return Value

Returns `true` if import is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Null was set to `strImportFilePath` parameter. |
| [System.ArgumentException](#) | Thrown when `strImportFilePath` is `empty` or file does not exist. |
