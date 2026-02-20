# CreateAutoCable(Project,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~CreateAutoCable(Project,String,Boolean).html

---

Automatically generate cables in the given project.

Syntax

**C#**



public void CreateAutoCable( 

   Project oProject,

   string strCreateSchemeName,

   bool bRegenrateConnections

)

public:

void CreateAutoCable( 

   Project^ oProject,

   String^ strCreateSchemeName,

   bool bRegenrateConnections

)


#### Parameters

*oProject*
:   Project in which cables will be generated.

*strCreateSchemeName*
:   Name of the scheme used for generating cables.

*bRegenrateConnections*
:   If set to true, connections are generated prior to cable generation.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | \Internal interface necessary for cable generation could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Cable generation has reported an error. Please read the exception message. |

Remarks

If the user scheme given in strCreateSchemeName does not exist, an ArgumentException will be thrown. If you pass an empty string to strCreateSchemeName, the last-used scheme will be used which is currently set in GUI.
