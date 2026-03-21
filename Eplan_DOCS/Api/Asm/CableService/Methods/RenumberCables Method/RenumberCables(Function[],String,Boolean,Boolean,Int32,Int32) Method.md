# RenumberCables(Function[],String,Boolean,Boolean,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1308.html

---

Method for numbering cables in a project.

Syntax

**C#**



public void RenumberCables( 

   Project oProject,

   string strNumberingSchemeName,

   bool bKeepOldNames,

   bool bKeepIdentifier,

   int nStartValue,

   int nStepValue

)

public:

void RenumberCables( 

   Project^ oProject,

   String^ strNumberingSchemeName,

   bool bKeepOldNames,

   bool bKeepIdentifier,

   int nStartValue,

   int nStepValue

)


#### Parameters

*oProject*
:   Project in which the cables will be numbered.

*strNumberingSchemeName*
:   Name of the scheme used for cable numbering.

*bKeepOldNames*
:   Keep existing cable DTs. If set to true, already existing cable DTs will not be changed, only cables with "?" character in the identifier will be numbered.

*bKeepIdentifier*
:   If set to true, the existing identifier will not be changed.

*nStartValue*
:   Start value for the device tag counter.

*nStepValue*
:   The device tag counter will be incremented by this value.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | The internal interface necessary for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. Please read the exception message.. |

Remarks

If the user scheme given in strNumberingSchemeName does not exist, an ArgumentException will be thrown. If you pass an empty string to strCreateSchemeName, the last-used scheme will be used which is currently set in GUI.
