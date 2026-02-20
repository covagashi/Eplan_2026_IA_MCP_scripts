# AbsoluteTransformation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AbsoluteTransformation.html

---

Absolute position and rotation represented by transformation matrix.

Syntax

**C#**



public Matrix3D AbsoluteTransformation {get; set;}

public:

property Matrix3D AbsoluteTransformation {

   Matrix3D get();

   void set (    Matrix3D value);

}


Remarks

Origin is lower left back corner, or in case of macros - origin is the same as in original CAD file. The default placement area is the XY-plane through Origin. Calculated in relation to origin of LayoutSpace coordinate system. Currently scaling 3d objects in P8 is not supported, therefore setting cell `M33` to value different then `1` may cause incorrect result.
