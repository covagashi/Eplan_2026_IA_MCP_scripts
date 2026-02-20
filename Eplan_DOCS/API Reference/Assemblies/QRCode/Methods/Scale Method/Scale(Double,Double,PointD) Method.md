# Scale(Double,Double,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode~Scale(Double,Double,PointD).html

---

Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter.

Syntax

**C#**



public override void Scale( 

   double fXAxis,

   double fYAxis,

   PointD ptOrigin

)

public:

void Scale( 

   double fXAxis,

   double fYAxis,

   PointD ptOrigin

) override


#### Parameters

*fXAxis*
:   X axis factor. E.g. value of 2 makes the width two times bigger.

*fYAxis*
:   Y axis factor. E.g. value of 0.5 makes the height two times smaller.

*ptOrigin*
:   Scaling origin point.

Exceptions

| Exception | Description |
| --- | --- |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when this method is called on an object that cannot be scaled. |

Remarks

Symbol references on pages of type other than graphical cannot be scaled. In such case an exception is thrown.
