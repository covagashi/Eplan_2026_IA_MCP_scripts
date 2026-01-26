# FindAllKeywords Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~FindAllKeywords.html

---

Finds all keywords selected by the searched text in given language.

Syntax

**C#**



public int FindAllKeywords( 

   string strTextToFind,

   ISOCode.Language eLang,

   ref List<MultiLangString> lstTexts,

   ref List<string> lstComments

)

public:

int FindAllKeywords( 

   String^ strTextToFind,

   ISOCode.Language eLang,

   List<MultiLangString^>^% lstTexts,

   List<String^>^% lstComments

)


#### Parameters

*strTextToFind*
:   Keyword to search for.

*eLang*
:   Language used for searching.

*lstTexts*
:   Texts from the found keywords.

*lstComments*
:   Comments from the found keywords.

#### Return Value

Number of found keywords.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an error. Please refer to the exception message. |

Remarks

Method finds keywords without exact matching, i.e these having strTextToFind as a part are also added to the result.
