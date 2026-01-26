# IsOnComponent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~IsOnComponent.html

---

If `true` then object is displayed next to its parent.

Syntax

**C#**



public bool IsOnComponent {get; set;}

public:

property bool IsOnComponent {

   bool get();

   void set (    bool value);

}


Remarks

If this property is set to `false` then contact image, depending on the selected plot frame, is displayed below or right on the page in the schematic path of the component.

If property [AutoAlign](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~AutoAlign.html) is false, then location is set manually and this property is not used by P8 to determine the location.
