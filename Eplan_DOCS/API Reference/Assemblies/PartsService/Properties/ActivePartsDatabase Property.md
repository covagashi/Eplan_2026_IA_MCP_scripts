# ActivePartsDatabase Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~ActivePartsDatabase.html

---

Returns or sets the type of current parts database. Possible values are PartsDatabaseType.SQL and PartsDatabaseType.EPLAN

Syntax

**C#**



public PartsService.PartsDatabaseType ActivePartsDatabase {get; set;}

public:

property PartsService.PartsDatabaseType ActivePartsDatabase {

   PartsService.PartsDatabaseType get();

   void set (    PartsService.PartsDatabaseType value);

}


Remarks

**SetSQLServerConnectionParameters**
