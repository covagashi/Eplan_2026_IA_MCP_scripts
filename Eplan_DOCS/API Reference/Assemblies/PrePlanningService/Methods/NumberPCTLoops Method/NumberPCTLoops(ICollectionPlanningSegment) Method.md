# NumberPCTLoops(ICollection<PlanningSegment>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~NumberPCTLoops(ICollection{PlanningSegment}).html

---

Numbers given PCTLoops. It is possible to number all PCTLoops in a given StructureSegment. Please look at the examples.

Syntax

**C#**



public void NumberPCTLoops( 

   ICollection<PlanningSegment> colObjects

)

public:

void NumberPCTLoops( 

   ICollection<PlanningSegment^>^ colObjects

)


#### Parameters

*colObjects*
:   Collection of objects to numerate. Can't be `null` or empty. Objects other then PCTLoop or StructureSegment are ignored.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `colObjects` is a `null` value. |
| [System.ArgumentException](#) | Thrown when collection `colObject` is empty or the objects in the collection belong to more than one project. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an Error occurred while numbering PCTLoops. |

Remarks

The objects in the parameter may only belong to one project otherwise a "System::ArgumentException" is thrown.

Example

The following examples shows how to use method NumberPCTLoops.

**C#**

```
//Numerate all PCTLoops in oStructureSegment1                

new PrePlanningService().NumberPCTLoops(new List<PlanningSegment>() { oStructureSegment1 });

```

**C#**

```
//Numerate two PCTLoops             

new PrePlanningService().NumberPCTLoops(new List<PlanningSegment>() { oPCTLoop2_1, oPCTLoop2_2 });

```
