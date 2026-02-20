# RelativeTransformationOfMacro Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RelativeTransformationOfMacro.html

---

Relative position and rotation represented by transformation matrix where transformation of macro is considered.

Syntax

**C#**



public Matrix3D RelativeTransformationOfMacro {get; set;}

public:

property Matrix3D RelativeTransformationOfMacro {

   Matrix3D get();

   void set (    Matrix3D value);

}


Remarks

Represents relative transformation including the macro transformation. Calculated in relation to origin of parent placement's coordinate system. For more information see the chapter: [API\_Pro\_Panel](API_Pro_Panel.html). Currently scaling 3d objects in P8 is not supported, therefore setting cell `M33` to value different then `1` may cause incorrect result.
