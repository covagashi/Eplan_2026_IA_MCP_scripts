# SegmentDefinition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~SegmentDefinition.html

---

Returns the [SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html) of the PlanningObject.

Syntax

**C#**



public virtual SegmentDefinition SegmentDefinition {get; set;}

public:

virtual property SegmentDefinition^ SegmentDefinition {

   SegmentDefinition^ get();

   void set (    SegmentDefinition^ value);

}


#### Property Value

PlanningSegment's [SegmentDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition.html).

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown while setting if new value is `null`. |
| [System.ArgumentException](#) | Thrown when new definition has different type then current definition. |
