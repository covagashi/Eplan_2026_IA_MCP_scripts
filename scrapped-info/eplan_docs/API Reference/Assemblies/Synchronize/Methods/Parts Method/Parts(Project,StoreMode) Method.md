# Parts(Project,StoreMode) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts(Project,StoreMode).html

---

Synchronizes the parts in the project to the parts master database. Updates parts database. Parts in the project are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize". Additionally the user can specify, whether parts, which are already existing in the parts database, should be modified.

Syntax

**C#**



public void Parts( 

   Project pProject,

   Synchronize.StoreMode storemode

)

public:

void Parts( 

   Project^ pProject,

   Synchronize.StoreMode storemode

)


#### Parameters

*pProject*
:   Project for which the parts will be synchronized.

*storemode*
:   Store mode determines, whether parts, which are already existing in the parts database, should be modified. The enumeration [Synchronize.StoreMode](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize+StoreMode.html) defines the supported values. If an invalid value is set, the value AppendNew = 0 will be used.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |
| **IOException** | Thrown in case of database write protection. |

Remarks

In order to have an article synchronized, it should exist as an entry in the project's parts or it should be referenced (i.e. exist as an ArticleReference).
