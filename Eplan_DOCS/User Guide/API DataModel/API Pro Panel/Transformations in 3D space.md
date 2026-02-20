# Transformations in 3D space

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Transformations_in_3D_space.html

---

Each  Placement3D  has 2 read-write properties that describe its transformation:

- Matrix3D Placement3D::AbsoluteTransformation  ' absolute transformation
- Matrix3D Placement3D::RelativeTransformation  ' transformation relative to a parent object

The properties are represented by a 4x4 transformation matrix:

M11      M12      M13     M14

M21      M22      M23     M24

M31      M32      M33     M34

OffsetX OffsetY OffsetZ M44

Here is an example of setting transformation matrix to a 3D object:

```csharp
Vector3D oVector3D = new Vector3D();
 oVector3D.X = 3.0;
 oVector3D.Y = 4.0;
 oVector3D.Z = 5.0;
 Quaternion oQuaternion = new Quaternion(oVector3D, 2.0);
 Matrix3D oMatrix3D = new Matrix3D();
 oMatrix3D.Rotate(oQuaternion);
 oMatrix3D.Translate(new Vector3D(1.0, 2.0, 3.0));
 oComponent1.AbsoluteTransformation = oMatrix3D;
```

It is also possible to move a 3D object using the  Move()  method:

```csharp
oComponent1.Move(1.0, 2.0, 3.0);
```

### How to calculate transformation relative to a specified 3D object

Sometimes it is necessary to calculate local transformation, i. e. relative to a specified 3D object.  
For example, it could be the position of components on a rail from its beginning:

To calculate the location of objects origin, it is necessary to use the  .RelativeTransformationOfMacro  property:

```csharp
Matrix3D terminalTransformation = terminal.RelativeTransformationOfMacro;
 var x_coordinate = terminalTransformation.Transform(new Point3D()).X;
```

 Another way is to use absolute transformation:

```csharp
Matrix3D railTransformation = rail.AbsoluteTransformation;
 railTransformation.Invert();
 var x_coordinate = railTransformation.Transform(terminal.AbsoluteTransformation.Transform(new Point3D()))).X;
```

### Rotation angle of a 3D object

 It can also be useful to get information about how an item was rotated during insertion from Placement options dialog:

To calculate this rotation, there should be used the  .RelativeTransformationOfMacro  property:

```csharp
Matrix3D matrix = oPlacement3D.RelativeTransformationOfMacro;
 double oRotationAngleZ = -1 * Math.Atan2(matrix.M21, matrix.M11) * (180.0 / Math.PI);
```
