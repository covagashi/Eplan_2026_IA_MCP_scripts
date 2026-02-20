# IsVisible Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice~IsVisible.html

---

Gets/Sets the actual visibility state of the function's graphical representation.

Syntax

**C#**



public bool IsVisible {get; set;}

public:

property bool IsVisible {

   bool get();

   void set (    bool value);

}


Remarks

Even if set to FALSE, this property will return TRUE when the 'Show invisible elements' setting of GED is on and when the placement's page is open.
