# ImportParts(String,String,ImportMode,Boolean,ImportIdentifier,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1524.html

---

Imports part to this database.

Syntax

**C#**



public void ImportParts( 

   string strFilePath,

   string strConverter,

   MDPartsDatabase.ImportMode mode,

   bool bAdditionalLanguage,

   MDPartsDatabase.ImportIdentifier importIdentifier,

   string strFieldMappingScheme

)

public:

void ImportParts( 

   String^ strFilePath,

   String^ strConverter,

   MDPartsDatabase.ImportMode mode,

   bool bAdditionalLanguage,

   MDPartsDatabase.ImportIdentifier importIdentifier,

   String^ strFieldMappingScheme

)


#### Parameters

*strFilePath*
:   Full file name

*strConverter*
:   Converter long name, see [XPamImport](XPamImport.html) for converters

*mode*
:   Import mode. The enumeration [MDPartsDatabase.ImportMode](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase+ImportMode.html) defines the supported values. If an invalid value is set, the value AppendNewRecords = 0 will be used.

*bAdditionalLanguage*
:   Specifies if multilanguage properties of records should be updated with another language rather then be replaced.

*importIdentifier*
:   Import Identifier. The enumeration [MDPartsDatabase.ImportIdentifier](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase+ImportIdentifier.html) defines the supported values.

*strFieldMappingScheme*
:   Specifies a field mapping scheme. This parameter may be an empty string in which case the scheme last used in GUI will be taken.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while importing parts data. |
