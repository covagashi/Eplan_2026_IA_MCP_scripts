# FillPattern Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Image~FillPattern.html

---

Gets or sets the fill pattern. Pattern types Bitmap, Eplan and System are not supported.

Syntax

**C#**



public override GraphicalPlacement.FillPatternType FillPattern {set;}

public:

property GraphicalPlacement.FillPatternType FillPattern {

   void set (    GraphicalPlacement.FillPatternType value) override;

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | The value cannot be set. |
