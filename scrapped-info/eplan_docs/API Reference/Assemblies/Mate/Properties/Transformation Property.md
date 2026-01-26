# Transformation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transformation.html

---

Position and rotation relative to the parent placement represented by transformation matrix.

Syntax

**C#**



public Matrix3D Transformation {get; set;}

public:

property Matrix3D Transformation {

   Matrix3D get();

   void set (    Matrix3D value);

}


Remarks

Please be aware that coordinates of a mate are relative if it is not persistent, i.e. without assigned Placement. Otherwise they are absolute, i.e. in relation to the point (0,0,0) of its InstallationSpace. Origin is the lower left corner of a placement area. If there isn't any user defined placement area, the default placement area is the XY-plane.
