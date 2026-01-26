# PCTLoop

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/PCTLoop.html

---

The  PCTLoop  class represents the PCT loops in a project. They are logical units to measure or control.

```csharp
SegmentDefinition oSegmentDefinition = m_oTestProject.GetSegmentDefinition("Eplan.PCT.Loop");
 PCTLoop oPCTLoop  = PCTLoop.Create(oSegmentDefinition) as PCTLoop;
```

In the GUI, they are visible in Pre-planning navigator:

