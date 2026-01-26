# OpenInstallationSpaceWithPlacement3D Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit3D~OpenInstallationSpaceWithPlacement3D.html

---

Opens the installation space and selects the Placement passed as oPlacement. The Placement is selected in the graphic editor.

Syntax

**C#**



public void OpenInstallationSpaceWithPlacement3D( 

   Placement3D oPlacement

)

public:

void OpenInstallationSpaceWithPlacement3D( 

   Placement3D^ oPlacement

)


#### Parameters

*oPlacement*
:   Placement to be selected.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Is thrown in case of null \parameters. |
| **ApplicationException** | The graphics editor interface could not be created. |
