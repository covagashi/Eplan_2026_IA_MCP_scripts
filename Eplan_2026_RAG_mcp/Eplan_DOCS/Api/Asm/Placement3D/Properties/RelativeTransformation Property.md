# RelativeTransformation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RelativeTransformation.html

---

Position and rotation relative to the parent placement represented by transformation matrix.

Syntax

**C#**



public Matrix3D RelativeTransformation {get; set;}

public:

property Matrix3D RelativeTransformation {

   Matrix3D get();

   void set (    Matrix3D value);

}


Remarks

Calculated in relation to origin of parent placementÃ¢'¬'¢s coordinate system. For more information see the chapter: [API\_Pro\_Panel](API_Pro_Panel.html). Currently scaling 3d objects in P8 is not supported, therefore setting cell `M33` to value different then `1` may cause incorrect result.
