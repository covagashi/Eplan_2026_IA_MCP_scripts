# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~Properties.html

---

.NET Property enabling access to P8 properties of the Page object.

Syntax

**C#**



public new DimensionItemPropertyList Properties {get;}

public:

new property DimensionItemPropertyList^ Properties {

   DimensionItemPropertyList^ get();

}


#### Property Value

P8 properties of the page.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.InsufficientLicenceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientLicenceException.html) | Thrown when no new logical page can be added to the project. |
