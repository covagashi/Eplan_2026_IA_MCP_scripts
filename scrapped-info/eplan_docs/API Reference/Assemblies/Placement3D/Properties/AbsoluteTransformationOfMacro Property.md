# AbsoluteTransformationOfMacro Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AbsoluteTransformationOfMacro.html

---

Absolute position and rotation represented by transformation matrix where transformation of macro is considered.

Syntax

**C#**



public Matrix3D AbsoluteTransformationOfMacro {get; set;}

public:

property Matrix3D AbsoluteTransformationOfMacro {

   Matrix3D get();

   void set (    Matrix3D value);

}


Remarks

Represents absolute transformation including the macro transformation. This is a transformation according to the default position of 3d object, i.e when it is inserted with coordinates 0,0,0 from GUI Calculated in relation to origin of LayoutSpace coordinate system. For more information see the chapter: [API\_Pro\_Panel](API_Pro_Panel.html). Currently scaling 3d objects in P8 is not supported, therefore setting cell `M33` to value different then `1` may cause incorrect result.
