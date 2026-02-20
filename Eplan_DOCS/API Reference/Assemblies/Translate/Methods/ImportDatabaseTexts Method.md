# ImportDatabaseTexts Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ImportDatabaseTexts.html

---

Importing text to translation database

Syntax

**C#**



public bool ImportDatabaseTexts( 

   string strFilename,

   string strConverter,

   string strReferenceLanguage

)

public:

bool ImportDatabaseTexts( 

   String^ strFilename,

   String^ strConverter,

   String^ strReferenceLanguage

)


#### Parameters

*strFilename*
:   Full file name.

*strConverter*
:   Converter long name, see [XPamImportXml](XPamImportXml.html) converters

*strReferenceLanguage*
:   List of language codes separated by semicolons.(example: en\_US;de\_DE)

#### Return Value

true, in case of no error.
