# Duct

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Duct.html

---

The  Duct  class represents ducts that hold cables in an organized manner and route them to the connected components.

```csharp
MountingPanel oMountingPanel = new MountingPanel();
 oMountingPanel.Create(m_oTestProject, 500.0, 400.0, 2.0);
 oMountingPanel.Parent = m_oInstallationSpace;
 Plane oPlane = oMountingPanel.Planes[0];
 Duct oDuct = new Duct();
 oDuct.Create(m_oTestProject, "KK3060", "1", 250.0);
 oDuct.Parent = oPlane;
 oDuct.FindSourceMate("M4", true).SnapTo(oPlane.GetTargetMates(true)[0] as PlaneMate, 0.0, 20.0, 300.0);
```

