# Working with parts database

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/WorkingWithPartsDataBase.html

---

The following example shows how to open the default parts database:

**C#**

```


MDPartsManagement oPartsManagement = new MDPartsManagement();

MDPartsDatabase partsDatabase = oPartsManagement.OpenDatabase();

```

It is also possible to open a selected parts database from a file:

**C#**

```


MDPartsDatabase partsDatabase = new MDPartsManagement().OpenDatabase("C:\\PathToDirectory\\DataBase.alk");

```

Then you can check information about the open database:

**C#**

```


// Show database name

var bdName = MDPartsManagement.SelectedPartsDatabaseAsString;

new Decider().Decide(EnumDecisionType.eOkDecision, bdName, "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Check if database is open

if (partsDatabase.IsOpen);

    new Decider().Decide(EnumDecisionType.eOkDecision, "DataBase is open", "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Check if database is readonly

if (!partsDatabase.IsReadOnly) ;

    new Decider().Decide(EnumDecisionType.eOkDecision, "DataBase is not readolny", "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

// Get database version

var dataBaseVersion = partsDatabase.Version;

// Get database type

var dataBaseType = partsDatabase.Type;

// Check if database scheme is up to date

if (partsDatabase.IsSchemeUpToDate) ;

  new Decider().Decide(EnumDecisionType.eOkDecision, "Scheme is up to date", "DB", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

```

Finally, close the database:

**C#**

```


partsDatabase.Close();

```