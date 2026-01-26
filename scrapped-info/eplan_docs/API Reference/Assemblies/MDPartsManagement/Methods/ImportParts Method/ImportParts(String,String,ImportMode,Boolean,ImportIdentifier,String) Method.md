# ImportParts(String,String,ImportMode,Boolean,ImportIdentifier,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1726.html

---

Imports parts to the system database.

Syntax

**C#**



public void ImportParts( 

   string strFilePath,

   string strConverter,

   MDPartsManagement.ImportMode mode,

   bool bAdditionalLanguage,

   MDPartsManagement.ImportIdentifier importIdentifier,

   string strFieldMappingScheme

)

public:

void ImportParts( 

   String^ strFilePath,

   String^ strConverter,

   MDPartsManagement.ImportMode mode,

   bool bAdditionalLanguage,

   MDPartsManagement.ImportIdentifier importIdentifier,

   String^ strFieldMappingScheme

)


#### Parameters

*strFilePath*
:   Full file name

*strConverter*
:   Converter long name, see [XPamImport](XPamImport.html) for converters

*mode*
:   Import mode. The enumeration [MDPartsManagement.ImportMode](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement+ImportMode.html) defines the supported values. If an invalid value is set, the value AppendNewRecords = 0 will be used.

*bAdditionalLanguage*
:   Specifies if multilanguage properties of records should be updated with another language rather then be replaced.

*importIdentifier*
:   Import Identifier. The enumeration [MDPartsManagement.ImportIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement+ImportIdentifier.html) defines the supported values.

*strFieldMappingScheme*
:   Specifies a field mapping scheme. This parameter may be an empty string in which case the scheme last used in GUI will be taken.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while importing parts data. |
