# Page Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InterruptionPointsFilter~Page.html

---

Sets the [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s matching the filter must be placed on.

Syntax

**C#**



public override Page Page {set;}

public:

property Page^ Page {

   void set (    Page^ value) override;

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
