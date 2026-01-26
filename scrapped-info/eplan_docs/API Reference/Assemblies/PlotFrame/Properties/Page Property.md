# Page Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFrame~Page.html

---

Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument.

Syntax

**C#**



public override Page Page {get;}

public:

property Page^ Page {

   Page^ get() override;

}


#### Property Value

Page of the placement. `null` if it is a transient placement.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the placement's page cannot be retrieved from the data model. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when it is not possible to place the placement on given page. |
| [System.ArgumentNullException](#) | Thrown when pPage is `null`. |

Remarks

In case of [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html) class setting Page property doesn't change the page for this placement.
