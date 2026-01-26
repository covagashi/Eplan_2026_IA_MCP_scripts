# SegmentPlacement

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/SegmentPlacement.html

---

The  SegmentPlacement  class represents segment objects on a 2D page. Because of this, the class inherits from  SymbolReference.

```csharp
// Prepare a segment
 StructureSegment oStructureSegment = StructureSegment.Create(m_oTestProject.SegmentDefinitions[0]) as StructureSegment;
 oStructureSegment.Name = "test1c";
 
 // Prepare a page
 Page oNewPage = new Page(m_oTestProject, DocumentTypeManager.DocumentType.Planning, new PagePropertyList());
 oNewPage.Name = "SegmentPlacement_Test001c";
           
 // Create SegmentPlacement
 SegmentPlacement oSegmentPlacement = new SegmentPlacement();
 oSegmentPlacement.Create(oStructureSegment, oNewPage);
```

SegmentPlacements  are visible in the GED, for example:

