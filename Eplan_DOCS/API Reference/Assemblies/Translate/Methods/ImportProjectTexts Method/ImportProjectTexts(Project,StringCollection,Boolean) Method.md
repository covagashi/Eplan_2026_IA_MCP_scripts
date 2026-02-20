# ImportProjectTexts(Project,StringCollection,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ImportProjectTexts(Project,StringCollection,Boolean).html

---

Method for importing texts from the project into the dictionary (language database). As the case may be, one or more new languages will be added to the dictionary. The language database into which the texts will be written are determined by a user setting. The languages specified in listLanguages should be already in the translation languages of the project, otherwise nothing is is imported for a language.

Syntax

**C#**



public bool ImportProjectTexts( 

   Project pProject,

   StringCollection listLanguages,

   bool bOverwrite

)

public:

bool ImportProjectTexts( 

   Project^ pProject,

   StringCollection^ listLanguages,

   bool bOverwrite

)


#### Parameters

*pProject*
:   Project from which the texts will be imported.

*listLanguages*
:   List of languages to import.

*bOverwrite*
:   If set to true, translations which are already existing in the dictionary will be overwritten by the imported texts.

#### Return Value

true, in case of no error.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs during import. |
