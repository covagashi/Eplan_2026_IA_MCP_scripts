# Scale Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~Scale.html

---

Scale used to display objects in ViewPlacement.

Syntax

**C#**



public double Scale {get; set;}

public:

property double Scale {

   double get();

   void set (    double value);

}


Remarks

Changing this value makes sense only if ViewScale is set to ViewScaleType.ScaleManual.

Changes are visible after calling [Update](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement~Update.html).
