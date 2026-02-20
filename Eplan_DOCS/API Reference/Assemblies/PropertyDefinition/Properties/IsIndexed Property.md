# IsIndexed Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsIndexed.html

---

Allows to check if a given property is indexed.

Syntax

**C#**



public bool IsIndexed {get;}

public:

property bool IsIndexed {

   bool get();

}


#### Property Value

'¢ true = Property is indexed

'¢ false = Property is not indexed

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when called for PropertyDefinition created as a conversion from other type. |

Remarks

Can only be called after retrieving a property list from the given API class.

Example

**C#**

```


Article article = myProject.Articles[0]; // A valid Article object

bool isIndexed = article.Properties.ARTICLE_HEIGHT.Definition.IsIndexed;

```
