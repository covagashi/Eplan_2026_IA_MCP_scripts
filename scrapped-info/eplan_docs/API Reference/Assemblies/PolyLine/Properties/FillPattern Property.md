# FillPattern Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PolyLine~FillPattern.html

---

Gets or sets the fill pattern of the PolyLine. Pattern types Bitmap, Eplan and System are not supported.

Syntax

**C#**



public GraphicalPlacement.FillPatternType FillPattern {get; set;}

public:

property GraphicalPlacement.FillPatternType FillPattern {

   GraphicalPlacement.FillPatternType get();

   void set (    GraphicalPlacement.FillPatternType value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | The value cannot be set. |
