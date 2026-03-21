# IsPlacementFilterActive Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsPlacementFilterActive.html

---

If true, then placement-filter is active.

Syntax

**C#**



public virtual bool IsPlacementFilterActive {get; set;}

public:

virtual property bool IsPlacementFilterActive {

   bool get();

   void set (    bool value);

}


Remarks

If active then framework uses **Eplan::EplApi::EServices::Ged::Interaction:** to determine if Placement should be included in selection.
