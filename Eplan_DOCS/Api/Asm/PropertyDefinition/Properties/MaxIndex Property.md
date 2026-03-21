# MaxIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~MaxIndex.html

---

Allows to check the maximum index of a given property.

Syntax

**C#**



public int MaxIndex {get;}

public:

property int MaxIndex {

   int get();

}


#### Property Value

Maximum index of a given property.

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

int maxIndex = article.Properties.ARTICLE_HEIGHT.Definition.MaxIndex;

```
