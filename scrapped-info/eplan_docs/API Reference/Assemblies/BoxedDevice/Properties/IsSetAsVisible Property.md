# IsSetAsVisible Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice~IsSetAsVisible.html

---

Gets/Sets visibility of the object as set in its properties dialog.

Syntax

**C#**



public override Placement.Visibility IsSetAsVisible {get; set;}

public:

property Placement.Visibility IsSetAsVisible {

   Placement.Visibility get() override;

   void set (    Placement.Visibility value) override;

}


Remarks

This property may return 'Invisible' even if the object is actually visible on the page because of the 'Show invisible elements' setting of GED.
