# SetFilteredPropertyList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencesFilter~SetFilteredPropertyList.html

---

Sets the [ArticleReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList.html) that [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching the filter must have.

Syntax

**C#**



public void SetFilteredPropertyList( 

   ArticleReferencePropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   ArticleReferencePropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties the [ArticleReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference.html)s matching the the filter. Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
