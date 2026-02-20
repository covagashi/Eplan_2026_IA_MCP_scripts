# ExportUntranslatableWords Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportUntranslatableWords.html

---

Export all untranslatable words from article database to file.

Syntax

**C#**



public void ExportUntranslatableWords( 

   ISOCode.Language[] languages,

   string strExportFilePath

)

public:

void ExportUntranslatableWords( 

   array<ISOCode.Language>^ languages,

   String^ strExportFilePath

)


#### Parameters

*languages*
:   Entries of these languages will be exported

*strExportFilePath*
:   Full file name of target file. Can't be `null` or `empty`.
