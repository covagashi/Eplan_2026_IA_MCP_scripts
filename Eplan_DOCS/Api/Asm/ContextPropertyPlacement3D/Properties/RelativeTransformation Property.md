# RelativeTransformation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.ContextPropertyPlacement3D~RelativeTransformation.html

---

Position relative to the parent represented by transformation matrix.

Syntax

**C#**



public Matrix3D RelativeTransformation {get; set;}

public:

property Matrix3D RelativeTransformation {

   Matrix3D get();

   void set (    Matrix3D value);

}


Remarks

Currently scaling 3d objects in P8 is not supported, therefore setting cell `M33` to value different then `1` may couse incorrect result.
