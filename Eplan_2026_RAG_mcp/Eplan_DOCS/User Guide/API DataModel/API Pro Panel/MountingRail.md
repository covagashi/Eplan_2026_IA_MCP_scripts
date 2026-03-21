# MountingRail

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/MountingRail.html

---

The MountingRail  is an item used to hold devices, usually attached to a Plane or [Cabinet](Cabinet.html).

```csharp
InstallationSpace oInstallationSpace = new InstallationSpace();
 oInstallationSpace.Create(m_oTestProject, "DataModel_081MountingRail_Test001");
 
 // Create a mounting panel
 MountingPanel oMountingPanel = new MountingPanel();
 oMountingPanel.Create(m_oTestProject, "MP AE 1057.500", "1");
 oMountingPanel.SetParent(oInstallationSpace, false);
 Plane oPlane1 = oMountingPanel.Planes[0];
 
 // Create a mounting rail
 MountingRail oMountingRail = new MountingRail();
 oMountingRail.Create(m_oTestProject, "TS 110_15", "1", 500.0);
 oMountingRail.SetParent(oPlane1, false);
 oMountingRail.FindSourceMate("M4", true).SnapTo(oPlane1.GetTargetMates(true)[0] as PlaneMate, 0.0, 10.0, 12.0);
```

