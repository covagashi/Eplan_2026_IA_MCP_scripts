# Methods

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString_methods.html

---

For a list of all members of this type, see [MultiLangString members](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString_members.html).

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~AddString.html) | Adds a string in the requested language. |
| Public Method | [Clear](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~Clear.html) | Removes the contents. |
| Public Method | [ContainsData](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~ContainsData.html) | Returns whether strings are saved in the MultiLanguageString. |
| Public Method | [DeleteAllStringsExceptFor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~DeleteAllStringsExceptFor.html) | Removes unused translations. |
| Public Method | [DeleteString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~DeleteString.html) | Deletes the language setting. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~Dispose().html) | Destructor for deterministic finalization of MultiLangString object. |
| Public Method | [GetAsString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~GetAsString.html) | Converts an MultiLangString to a string. The languages are appended to one another, all having the same format. |
| Public Method | [GetLanguageList](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~GetLanguageList.html) | Returns the list of the languages currently saved in this [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [GetString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~GetString.html) | Returns the string in the requested language |
| Public Method | [GetStringToDisplay](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~GetStringToDisplay.html) | Returns the string that is to be displayed in accordance with the passed language. This may be the string saved for this language or, if there is no such string, a language-independent string. |
| Public Method | [IsEqual](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~IsEqual.html) | Compares every string in every language. If a string is different in one language, then == returns FALSE. If an language string exists in one of the MultiLangStrings but not in the others, this function returns FALSE even if the language string is empty. |
| Public Method | [SetAsString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~SetAsString.html) | Sets the contents of a MultiLangString with a string passed as argument using language marker if necessary. If argument is in MultiLangString form, it will be parsed and saved under given languages. Otherwise '??\_??@' prefix is added which means that the object is visible the same in every language. |
| Public Method | [ToString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~ToString.html) | Returns a string that represents the current object. |
| Public Method | [Translatable](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString~Translatable.html) | Indicates whether the MultiLanguageString can be translated. |


