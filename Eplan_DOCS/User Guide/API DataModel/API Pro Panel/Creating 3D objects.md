# Creating 3D objects

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Creating_3D_objects.html

---

Creating most 3D objects is done by using an article number and variant. The example below shows how to create and place a cabinet in the  InstallationSpace.

```csharp
Cabinet oCabinet = new Cabinet();
 oCabinet.Create(oProject, "TS 8886.500", "1");
 // Parent will be set to installation space
 oCabinet.Parent = oProject.InstallationSpaces[0];
 // Create identity matrix
 System.Windows.Media.Media3D.Matrix3D oMatrix = new System.Windows.Media.Media3D.Matrix3D();
 // Change the location to (100, 150, 0)
 oMatrix.Transform(new System.Windows.Media.Media3D.Point3D(100, 150, 0));
 oCabinet.AbsoluteTransformation = oMatrix;
```