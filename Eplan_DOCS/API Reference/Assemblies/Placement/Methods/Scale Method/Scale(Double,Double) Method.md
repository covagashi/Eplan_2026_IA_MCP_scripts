# Scale(Double,Double) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale(Double,Double).html

---

Scales the placement (or group of placements) by the specified factors in X and Y axis.

Syntax

**C#**



public virtual void Scale( 

   double fXAxis,

   double fYAxis

)

public:

virtual void Scale( 

   double fXAxis,

   double fYAxis

)


#### Parameters

*fXAxis*
:   X axis factor. E.g. value of 2 makes the width two times bigger.

*fYAxis*
:   Y axis factor. E.g. value of 0.5 makes the height two times smaller.

Exceptions

| Exception | Description |
| --- | --- |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when this method is called on an object that cannot be scaled. |

Remarks

When using this method, the scaling origin point is (0, 0). Symbol references on pages of type other than graphical cannot be scaled. In such case an exception is thrown.
