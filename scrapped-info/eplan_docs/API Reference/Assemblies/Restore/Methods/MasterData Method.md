# MasterData Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Restore~MasterData.html

---

Restore master data from archive files.

Syntax

**C#**



public void MasterData( 

   string strArchivename,

   string strRestorePath

)

public:

void MasterData( 

   String^ strArchivename,

   String^ strRestorePath

)


#### Parameters

*strArchivename*
:   Name of the archive to be restored.

*strRestorePath*
:   Path into which the projects will be restored.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred, when restoring master data. |
| **ApplicationException** | \Internal interface for restore could not be created. |

Remarks

If the master data to restore already exist, they will not be overwritten.
