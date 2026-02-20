# Translate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate.html

---

Class providing functionality for translating project data.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.Translate**

Syntax

**C#**



public class Translate

public ref class Translate

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Translate Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~_ctor.html) | Default constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ActiveTranslateDatabase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ActiveTranslateDatabase.html) | Returns or sets the type of current translate database. Possible values are DatabaseType.SQL and DatabaseType.EPLAN |
| Public Property | [TranslateDatabase](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateDatabase.html) | Returns or sets the complete filename of the current translate database or connection string if SQL connection is selected. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddProjectLanguage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~AddProjectLanguage.html) | Overloaded. Method for adding a project language. It adds the language to the set of possible languages. |
| Public Method | [Correct](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~Correct.html) | Overloaded. Correct translations in project. |
| Public Method | [Dispose](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~Dispose().html) | Destructor |
| Public Method | [ExportDatabaseTexts](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ExportDatabaseTexts.html) | Exporting text from translation database |
| Public Method | [ExportMissingTranslation](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ExportMissingTranslation.html) | Overloaded. Exports a missing-word list of the given objects. |
| Public Method | [GetCommonLanguages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~GetCommonLanguages.html) | Determines the list of languages, which the given storableObjects have in common. Is used for getting the common languages of a project. |
| Public Method | [GetStringToDisplayInDialogs](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~GetStringToDisplayInDialogs.html) | Overloaded. Get string displayed in project-independent dialogs (like parts management). |
| Public Method | [ImportDatabaseTexts](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ImportDatabaseTexts.html) | Importing text to translation database |
| Public Method | [ImportProjectTexts](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~ImportProjectTexts.html) | Overloaded. Method for importing texts from the project into the dictionary (language database). As the case may be, one or more new languages will be added to the dictionary. The language database into which the texts will be written are determined by a user setting. The languages specified in listLanguages should be already in the translation languages of the project, otherwise nothing is is imported for a language. |
| Public Method | [RemoveProjectLanguage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~RemoveProjectLanguage.html) | Overloaded. Method for removing a project language. It removes the language from the set of displayed languages. |
| Public Method | [RemoveProjectLanguages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~RemoveProjectLanguages.html) | Method for removing a collection of languages from a project. |
| Public Method | [SetDisplayedLanguages](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~SetDisplayedLanguages.html) | Overloaded. Method for adding a language that will be displayed in the project. |
| Public Method | [SetSQLServerConnectionParameters](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~SetSQLServerConnectionParameters.html) | Sets SQL connection parameters. |
| Public Method | [TranslateObjects](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateObjects.html) | Translates all texts of a StorableObject (also project or page). |
| Public Method | [TranslatePage](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslatePage.html) | Translates all texts of a page in the specified project. |
| Public Method | [TranslateProject](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateProject.html) | Translates all texts in the specified project. |
| Public Method | [TranslateText](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Translate~TranslateText.html) | Get translation for the given text, according to project settings. |


