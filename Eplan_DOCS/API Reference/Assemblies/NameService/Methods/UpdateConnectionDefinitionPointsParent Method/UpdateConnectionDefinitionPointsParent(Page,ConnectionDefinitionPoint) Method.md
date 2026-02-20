# UpdateConnectionDefinitionPointsParent(Page,ConnectionDefinitionPoint) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1393.html

---

Sets the page and updates the graphical parent of a connection definition point

Syntax

**C#**



public void UpdateConnectionDefinitionPointsParent( 

   Page pPage,

   ConnectionDefinitionPoint pCDP

)

public:

void UpdateConnectionDefinitionPointsParent( 

   Page^ pPage,

   ConnectionDefinitionPoint^ pCDP

)


#### Parameters

*pPage*
:   Page to set.

*pCDP*
:   Connection definition point for updates the graphical parent.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
