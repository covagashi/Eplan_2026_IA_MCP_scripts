# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~Properties.html

---

Represents ArticleReference properties

Syntax

**C#**



public new ArticleReferencePropertyList Properties {get;}

public:

new property ArticleReferencePropertyList^ Properties {

   ArticleReferencePropertyList^ get();

}


Remarks

Properties from `ArticleReferencePropertyList` have another ids than these from parent object or in the 'Part reference data' tab in GUI. In order to use the same ids as in GUI, please use parent object ids (see the first example). When accessing user-defined property by a parent object, there is necessary to add 'EPLAN.ArticleRef.' prefix to its identifying name. Also there must by the index provided which is position of an ArticleReference at a parent object.

Example

Setting article reference properties by parent object ids Setting article reference properties by ArticleReferencePropertyList ids Getting article reference user-defined property by parent object

**C#**

```
articleReference.ParentObject.Properties[Properties.Function.FUNC_ARTICLE_NOTE, 1] = "ARTICLE_NOTE3";

string note = articleReference.ParentObject.Properties[Properties.Function.FUNC_ARTICLE_NOTE, 1];
```

**C#**

```
articleReference.Properties[Properties.ArticleReference.ARTICLE_NOTE] = "note";

string note = articleReference.Properties[Properties.ArticleReference.ARTICLE_NOTE];
```

**C#**

```
var propertyValue = project.Properties["EPLAN.ArticleRef.UserProperty.1"][1].ToString();
```
