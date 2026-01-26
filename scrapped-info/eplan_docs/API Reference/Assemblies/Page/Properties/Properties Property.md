# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Properties.html

---

Property enabling access to internal properties of the Page object.

Syntax

**C#**



public new PagePropertyList Properties {get;}

public:

new property PagePropertyList^ Properties {

   PagePropertyList^ get();

}


#### Property Value

Eplan properties of the page.

Exceptions

| Exception | Description |
| --- | --- |
| [InsufficientLicenceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientLicenceException.html) | Thrown when no new logical page can be added to the project. |

Example

**C#**

```
Page page = oProject.Pages[10];

page.Properties.PAGE_REVISION_APPROVEDBY = "John";

string strCounter = page.Properties.PAGE_COUNTER;
```
