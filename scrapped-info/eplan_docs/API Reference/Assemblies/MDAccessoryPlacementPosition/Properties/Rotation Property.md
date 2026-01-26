# Rotation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacementPosition~Rotation.html

---

Rotation angle.

Syntax

**C#**



public double Rotation {get; set;}

public:

property double Rotation {

   double get();

   void set (    double value);

}


Remarks

Value of rotation angle is given in degrees. The range of possible rotation angle values is from -360 degrees to 360 degrees. Setter of this property converts passed value so that it falls in the possible range. Value is taken and stored in property called EW3\_PROPERTY\_ARTICLEACCESSORYPLACEMENTPOSITION\_ROTATION.
