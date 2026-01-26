# SystemEntries Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~SystemEntries.html

---

Returns the file names of all master data in the system master data pool.

Syntax

**C#**



public StringCollection SystemEntries {get;}

public:

property StringCollection^ SystemEntries {

   StringCollection^ get();

}


Exceptions

| Exception | Description |
| --- | --- |
| **ApplicationException** | Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | System master data files could not be returned correctly. |
