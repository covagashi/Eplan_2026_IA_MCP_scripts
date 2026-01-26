# ExportMissingTranslation(String,String,StringCollection,StorableObject[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1462.html

---

Exports a missing-word list of the given objects.

Syntax

**C#**



public bool ExportMissingTranslation( 

   string strFilename,

   string strConverter,

   StringCollection listLanguages,

   StorableObject[] storableObjects

)

public:

bool ExportMissingTranslation( 

   String^ strFilename,

   String^ strConverter,

   StringCollection^ listLanguages,

   array<StorableObject^>^ storableObjects

)


#### Parameters

*strFilename*
:   \File name of the missing\-word list file.

*strConverter*
:   Format of the export file defined by the name of the XML converter to use\:

    XTrLanguageDbXml2TabConverterImpl \- export as tab\-separated Unicode\-File (Eplan 21 format)

*listLanguages*
:   List of languages, for which the missing translations will be exported.

*storableObjects*
:   Array of StorableObjects, for which the missing translations will be exported.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. invalid objects in the `storableObjects` array. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an error occurred during export. |

Remarks

All languages in listLanguages have to be already in the list of translation languages of the project.
