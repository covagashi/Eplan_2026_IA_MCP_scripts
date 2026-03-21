# CanSnapTo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PointMate~CanSnapTo.html

---

Check, if this mate can snap to targetMate

Syntax

**C#**



public bool CanSnapTo( 

   Mate pTargetMate

)

public:

bool CanSnapTo( 

   Mate^ pTargetMate

)


#### Parameters

*pTargetMate*

#### Return Value

Returns true, if snapping is possible

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |

Remarks

Snapping is only possible if the typename of the target name is one of the matching mates of this mate
