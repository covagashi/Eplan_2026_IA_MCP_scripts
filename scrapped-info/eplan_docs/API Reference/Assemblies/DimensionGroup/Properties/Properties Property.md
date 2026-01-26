# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DimensionGroup~Properties.html

---

.NET Property enabling access to P8 properties of the Page object.

Syntax

**C#**



public new DimensionGroupPropertyList Properties {get;}

public:

new property DimensionGroupPropertyList^ Properties {

   DimensionGroupPropertyList^ get();

}


#### Property Value

P8 properties of the page.

Exceptions

| Exception | Description |
| --- | --- |
| [InsufficientLicenceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientLicenceException.html) | Thrown when no new logical page can be added to the project. |
