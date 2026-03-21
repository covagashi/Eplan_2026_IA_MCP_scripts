# Parts(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~Parts(String).html

---

Synchronizes the parts in the project to the parts master database. Updates parts database. When there is a reference to a part in a project, and the part is not in the project, then after invoking oSynchronize.Parts(oProject), this part becomes stored in the project (Project.Articles increases by 1), in other case parts in the project are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize".

Syntax

**C#**



public void Parts( 

   string strFullLinkFileName

)

public:

void Parts( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project for which the parts will be synchronized.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |
| **IOException** | Thrown in case of database write protection. |

Remarks

The specified project may be open in EPLAN or not. If the project is not opened from the beginning, it will be opened for the synchronization process and will be closed subsequently. In order to have an article synchronized, it should exist as an entry in the project's parts or it should be referenced (i.e. exist as an ArticleReference).
