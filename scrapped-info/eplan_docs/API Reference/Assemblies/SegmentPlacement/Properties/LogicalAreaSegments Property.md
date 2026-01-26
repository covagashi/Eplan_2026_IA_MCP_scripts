# LogicalAreaSegments Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement~LogicalAreaSegments.html

---

Gets/Sets an array of segments that the symbol's logical area may consist of.

Syntax

**C#**



public override SymbolReference.Segment[] LogicalAreaSegments {set;}

public:

property array<SymbolReference.Segment^>^ LogicalAreaSegments {

   void set (    array<SymbolReference.Segment^>^ value) override;

}


Remarks

Note: After setting the logical area with the [Eplan.EplApi.DataModel.SymbolReference.SetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SetLogicalArea.html) method this property returns an array containing 3 segments (that represent a rectangular area)
