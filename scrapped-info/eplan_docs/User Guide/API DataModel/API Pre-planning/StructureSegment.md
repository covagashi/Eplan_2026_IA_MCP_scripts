# StructureSegment

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/StructureSegment.html

---

The  StructureSegment  class represents structure segment objects. They are used to represent a part of the project structure.

```csharp
SegmentDefinition oSegmentDefinition = m_oTestProject.GetSegmentDefinition("Eplan.Base.StructureNode");
 StructureSegment oStructureSegment = StructureSegment.Create(m_oTestProject.SegmentDefinitions[0]) as StructureSegment;
 oStructureSegment.Name = "test1b";
```

 In the GUI, they are visible in Pre-planning navigator:

