# GetUncompletedInstallationSpaces Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~GetUncompletedInstallationSpaces.html

---

Returns an array of modified and not completed installation spaces in the current revision of a project. Used for change tracking.

Syntax

**C#**



public InstallationSpace[] GetUncompletedInstallationSpaces( 

   Project oProject

)

public:

array<InstallationSpace^>^ GetUncompletedInstallationSpaces( 

   Project^ oProject

)


#### Parameters

*oProject*
:   A project to get the installation spaces from.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. In case of a project on which no "Complete project" operation was called (from API or GUI), an empty array will be returned. When a revision for a project section is active, only the installation spaces of this project section are returned.
