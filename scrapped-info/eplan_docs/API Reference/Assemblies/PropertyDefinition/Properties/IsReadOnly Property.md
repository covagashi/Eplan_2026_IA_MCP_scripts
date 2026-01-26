# IsReadOnly Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsReadOnly.html

---

Allows to check if a given property is read-only.

Syntax

**C#**



public bool IsReadOnly {get;}

public:

property bool IsReadOnly {

   bool get();

}


#### Property Value

'¢ true = Property is read-only

'¢ false = Property is not read-only

Remarks

Can only be called after retrieving a property list from the given API class.

Example

**C#**

```


Article article = myProject.Articles[0]; // A valid Article object

bool isReadOnly = article.Properties.ARTICLE_HEIGHT.Definition.IsReadOnly;

```
