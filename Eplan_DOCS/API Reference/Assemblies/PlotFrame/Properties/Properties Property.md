# Properties Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFrame~Properties.html

---

.NET Property enabling access to P8 properties of the PlotFrame object.

Syntax

**C#**



public new PlotFramePropertyList Properties {get;}

public:

new property PlotFramePropertyList^ Properties {

   PlotFramePropertyList^ get();

}


#### Property Value

P8 properties of the plotframe.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.InsufficientLicenceException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InsufficientLicenceException.html) | Thrown when no new logical plotframe can be added to the project. |

Example

**C#**

```
PlotFrame oPlotFrame;

String pfGridOffsetX = oPlotFrame.Properties.FRAME_EVALUATION_AREA_START_POINT_X.ToString();

String pfGridOffsetY = oPlotFrame.Properties.FRAME_EVALUATION_AREA_START_POINT_Y.ToString();

String pfColWidth1 = oPlotFrame.Properties.FRAME_PATHSIZE[1].ToString();

String pfColWidth2 = oPlotFrame.Properties.FRAME_PATHSIZE[1].ToString();
```
