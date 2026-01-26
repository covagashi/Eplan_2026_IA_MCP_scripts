# Scale(Double,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.QRCode~Scale(Double,PointD).html

---

Scales the QRCode by the specified factor in X and Y axis with scaling origin point specified by the ptOrigin parameter.

Syntax

**C#**



public void Scale( 

   double factor,

   PointD ptOrigin

)

public:

void Scale( 

   double factor,

   PointD ptOrigin

)


#### Parameters

*factor*
:   Scaling factor. E.g. value of 2 makes the width two times bigger.

*ptOrigin*
:   Scaling origin point.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when this method is called on an object that cannot be scaled. |
