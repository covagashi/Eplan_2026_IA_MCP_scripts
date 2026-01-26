# UpdateConnectionDefinitionPointsParent(ConnectionDefinitionPoint) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1394.html

---

Updates the graphical parent of a connection definition point.

Syntax

**C#**



public void UpdateConnectionDefinitionPointsParent( 

   ConnectionDefinitionPoint pCDP

)

public:

void UpdateConnectionDefinitionPointsParent( 

   ConnectionDefinitionPoint^ pCDP

)


#### Parameters

*pCDP*
:   Connection definition point for updates the graphical parent.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters were found. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | When page is not set. |
