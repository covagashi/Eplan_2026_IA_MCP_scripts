# CompleteInstallationSpaces Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Revision~CompleteInstallationSpaces.html

---

Completes modification of installation spaces in the current revision of a project. Used for change tracking.

Syntax

**C#**



public void CompleteInstallationSpaces( 

   InstallationSpace[] spacesToComplete,

   string strIndex,

   string strRevDescription,

   string strReasonOfChange

)

public:

void CompleteInstallationSpaces( 

   array<InstallationSpace^>^ spacesToComplete,

   String^ strIndex,

   String^ strRevDescription,

   String^ strReasonOfChange

)


#### Parameters

*spacesToComplete*
:   An array of installation spaces to complete.

*strIndex*
:   Name of the new revision.

*strRevDescription*
:   Description of the new revision.

*strReasonOfChange*
:   Additional description of the new revision.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid parameters. |
| **ApplicationException** | Internal interface necessary for the revision management could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the action. |

Remarks

Used for change tracking. When a logging revision starts, every changed installation space gets the marker "Draft" on it. With this function an installation space is completed, a revision is created (visible in the revision properties) and the draft is removed. When the revision belongs to an active project section, only the installation spaces of this section are completed.
