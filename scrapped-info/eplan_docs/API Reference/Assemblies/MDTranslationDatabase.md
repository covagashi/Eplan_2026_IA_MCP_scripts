# MDTranslationDatabase

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase.html

---

Represents translation database.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDTranslationDatabase**

Syntax

**C#**



public class MDTranslationDatabase

public ref class MDTranslationDatabase


Example

Following example shows how to use TranslationDatabase class.

**C#**

```
private static bool ReplaceText(string strSearchedText, ISOCode.Language eSearchedLang, string strTextToChange, ISOCode.Language eLangToChange)

{

    bool bRetVal;

    MDTranslationDatabase oTrDB = new MDTranslationDatabase();

    oTrDB.Open(false);

    MultiLangString oMLS = new MultiLangString();

    oMLS.AddString(eSearchedLang, strSearchedText);

    string strComment = "";

    bRetVal = oTrDB.FindKeyword(eSearchedLang, ref oMLS, ref strComment);

    if (bRetVal)

    {

        oMLS.DeleteString(eLangToChange);

        oMLS.AddString(eLangToChange, strTextToChange);

        LanguageList lstLangs = new LanguageList();

        lstLangs.Add(eLangToChange);

        bRetVal = oTrDB.EditKeyword(strSearchedText, eSearchedLang, oMLS, lstLangs);

    }

    oTrDB.Close();

    return bRetVal;

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDTranslationDatabase Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~_ctor.html) | Constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [IsOpen](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~IsOpen.html) | Returns true if database is open. |
| Public Property | [IsReadOnly](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~IsReadOnly.html) | Returns true if database is opened in readonly mode. |
| Public Property | [Languages](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~Languages.html) | Returs the list of translation database languages. |
| Public Property | [NotTranslatedWords](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~NotTranslatedWords.html) | Gets all not translated words. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddKeyword](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~AddKeyword.html) | Overloaded. Adds keywords with texts in specified languages to the translation database. |
| Public Method | [AddLanguage](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~AddLanguage.html) | Adds new translation database language. |
| Public Method | [Close](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~Close.html) | Closes database. |
| Public Method | [DeleteKeyword](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~DeleteKeyword.html) | Deletes keyword. |
| Public Method | [DeleteLanguage](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~DeleteLanguage.html) | Deletes translation database language. |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~Dispose().html) | Destructor for deterministic finalization of TranslationDatabase object. |
| Public Method | [EditKeyword](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~EditKeyword.html) | Overloaded. Edits keyword |
| Public Method | [FindAllKeywords](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~FindAllKeywords.html) | Finds all keywords selected by the searched text in given language. |
| Public Method | [FindKeyword](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~FindKeyword.html) | Finds keyword. |
| Public Method | [Open](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDTranslationDatabase~Open.html) | Opens translation database using user settings. |


