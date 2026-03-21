# WriteProtected Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~WriteProtected.html

---

Checks if an object is currently write protected or sets manual write protection

Syntax

**C#**



bool WriteProtected {get; set;}

property bool WriteProtected {

   bool get();

   void set (    bool value);

}


#### Property Value

true : if object is currently write-protected

false : if no write protection was set or when write protection was disabled

Exceptions

| Exception | Description |
| --- | --- |
| [WriteProtectionChangeNotAllowed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.WriteProtectionChangeNotAllowed.html) | Thrown because of current write protection state; no further modifications are allowed. |
