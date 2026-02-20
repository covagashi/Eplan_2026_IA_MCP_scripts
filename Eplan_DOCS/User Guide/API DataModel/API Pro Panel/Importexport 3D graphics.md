# Import/export 3D graphics

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Import_export_3G_graphics.html

---

### Export

Export of 3D graphics is possible to the  STEP  or the  VRML  format:

Export3D::ProjectToStep                          ' Exports all installation spaces from a project.

Export3D::InstallationSpacesToStep  ' Exports installation spaces.

Export3D::ProjectToVrml                          ' Exports all installation spaces from a project.

Export3D::InstallationSpacesToVrml  ' Exports installation spaces.

### Import

The item data must be available in the common international  STEP  format (Standard for the Exchange of Product model data).

For each import, a new layout space is generated with the name of the imported  STEP  file.

```csharp
InstallationSpace oInstallationSpace = new Import().Graphics3D(oProject, "c:\\temp\\BK3100\\BK3xxx.stp");

```