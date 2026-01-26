# UpgradePartsDb(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~UpgradePartsDb(String).html

---

Upgrades parts database.

Syntax

**C#**



public void UpgradePartsDb( 

   string strPartsDatabase

)

public:

void UpgradePartsDb( 

   String^ strPartsDatabase

)


#### Parameters

*strPartsDatabase*
:   Old database name. Full path to .mdb database or connection string to SQL database.

Remarks

This method migrates SQL or .mdb databases from a format prior to v2022 to the current format.  
  
OpenDatabase method does not automatically update a parts database from a previous to the current version. Databases in an older format will be opened read-only. You can check whether the database format is up-to-date by the property MDPartsDatabase.IsSchemeUpToDate and update it if needed by the method MDPartsDatabase.UpdateScheme(). Parts databases prior to version 2022 need to be upgraded / converted either manually, using this method or by the action XPamConvertPartDatabaseToArticleDatabaseAction /OldDatabase... /NewDatabase...
