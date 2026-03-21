# ChamferRadius Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Rectangle~ChamferRadius.html

---

Returns radius of Rectangle's corners chamfers.

Syntax

**C#**



public virtual double ChamferRadius {get; set;}

public:

virtual property double ChamferRadius {

   double get();

   void set (    double value);

}


#### Property Value

radius of chamfers in mm.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the radius cannot be read. |
