# Rotation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.TextBase~Rotation.html

---

Returns the rotation of the Text, in radians.

Syntax

**C#**



public double Rotation {get; set;}

public:

property double Rotation {

   double get();

   void set (    double value);

}


#### Property Value

rotation of the Text, in radians

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when rotation cannot be read |

Remarks

Please note that -16002.0 is used as "From layer" value.
