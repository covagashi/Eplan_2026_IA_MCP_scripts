# Drilling

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Drilling_(Cut-out_in_GUI).html

---

The  Drilling  class represents the opening in construction items such as mounting panels and sheets, that are drilled or manufactured by NC robots.

```csharp
Drilling oDrillingHole = Drilling.CreateTapHole(oProject, 50.0, null);
 oDrillingHole.SetParent(oPlane, true);
 oDrillingHole.GetSourceMates(true)[0].SnapTo(oPlane.GetTargetMates(true)[0] as PlaneMate, 0.0, 0.0, 0.0);
 
 Drilling oDrillingHexagon = Drilling.CreateHexagon(oProject, 75.0, null);
 oDrillingHexagon.SetParent(oPlane, true); oDrillingHexagon.GetSourceMates(true)[0].SnapTo(oPlane.GetTargetMates(true)[0] as PlaneMate, 40.0, 30.0, 50.0);
```

