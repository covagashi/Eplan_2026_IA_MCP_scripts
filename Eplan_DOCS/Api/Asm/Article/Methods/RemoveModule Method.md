# RemoveModule Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Article~RemoveModule.html

---

Removes module from article.

Syntax

**C#**



public void RemoveModule( 

   Article.Module pModule

)

public:

void RemoveModule( 

   Article.Module^ pModule

)


#### Parameters

*pModule*
:   Module which will be removed. After removing objects becomes invalid.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `pModule` is `null` or invalid. |

Remarks

Modification of modules collection assigned to article is done only in project database. Changes are `not` visible in system parts database until synchronization of parts is done.
