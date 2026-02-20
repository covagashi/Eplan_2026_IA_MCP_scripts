# OpenDatabase() Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~OpenDatabase().html

---

Opens the parts database configured in the settings.

Syntax

**C#**



public MDPartsDatabase OpenDatabase()

public:

MDPartsDatabase^ OpenDatabase();


Remarks

OpenDatabase method does not automatically update a parts database from a previous to the current version. Databases in an older format will be opened read-only. You can check whether the database format is up-to-date by the property MDPartsDatabase.IsSchemeUpToDate and update it if needed by the method MDPartsDatabase.UpdateScheme(). Parts databases prior to version 2022 need to be upgraded / converted either manually or by the action XPamConvertPartDatabaseToArticleDatabaseAction /OldDatabase... /NewDatabase...
