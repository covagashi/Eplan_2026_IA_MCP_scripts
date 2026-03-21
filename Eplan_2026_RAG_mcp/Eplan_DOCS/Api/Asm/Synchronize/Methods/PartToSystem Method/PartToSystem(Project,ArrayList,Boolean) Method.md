# PartToSystem(Project,ArrayList,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PartToSystem(Project,ArrayList,Boolean).html

---

Synchronizes the specified parts into the parts master database. Updates parts database. Parts in the project are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize" for selected parts.

Syntax

**C#**



public void PartToSystem( 

   Project oProject,

   ArrayList lParts,

   bool bUseNotReferencedArticles

)

public:

void PartToSystem( 

   Project^ oProject,

   ArrayList^ lParts,

   bool bUseNotReferencedArticles

)


#### Parameters

*oProject*
:   Project for which the parts will be synchronized.

*lParts*
:   List of parts (objects of type [Eplan.EplApi.DataModel.Article](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article.html) or [Eplan.EplApi.DataModel.ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)) that will be synchronized.

*bUseNotReferencedArticles*
:   Specifies that not referenced articles are synchronized.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |
| **IOException** | Thrown in case of database write protection. |

Remarks

Method calls PartToSystem(oProject, lParts, StoreMode::AppendNew, true) internally. In order to have an article synchronized, it should exist as an entry in the project's parts or it should be referenced (i.e. exist as an ArticleReference).
