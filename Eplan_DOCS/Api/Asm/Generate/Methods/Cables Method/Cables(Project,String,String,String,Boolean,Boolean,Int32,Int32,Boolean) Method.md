# Cables(Project,String,String,String,Boolean,Boolean,Int32,Int32,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1362.html

---

Creates cables in the given project. The functionality includes three steps: creating cables, cable numbering, cable selection.

Syntax

**C#**



public void Cables( 

   Project oProject,

   string strCreateSchemaName,

   string strNumberingSchemaName,

   string strAutoSelSchemaName,

   bool bRegenrateConnections,

   bool bKeepOldNames,

   int nStartValue,

   int nStepValue,

   bool bOnlyAutomaticCables

)

public:

void Cables( 

   Project^ oProject,

   String^ strCreateSchemaName,

   String^ strNumberingSchemaName,

   String^ strAutoSelSchemaName,

   bool bRegenrateConnections,

   bool bKeepOldNames,

   int nStartValue,

   int nStepValue,

   bool bOnlyAutomaticCables

)


#### Parameters

*oProject*
:   Project in which cables will be generated.

*strCreateSchemaName*
:   Name of the scheme for generating cables.

*strNumberingSchemaName*
:   Name of the scheme for cable numbering.

*strAutoSelSchemaName*
:   Name of the scheme for automatic cable selection.

*bRegenrateConnections*
:   If set to true, connections are updated in advance to cable generation.

*bKeepOldNames*
:   If set to true, existing cable names are not changed.

*nStartValue*
:   Start value of the device tag counter.

*nStepValue*
:   Step width, by which the DT counter is increased.

*bOnlyAutomaticCables*
:   If set to true, the cable selection will only be done for automatically created cables.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments, for example a wrong scheme. |
| **ApplicationException** | An internal interface necessary for generating cables could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during cable generation. Please refer to the exception message. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |

Remarks

If you pass an empty string to a scheme parameter, the last used scheme will be used which is currently set in GUI. If no scheme does exist under the given scheme name, an exception will be thrown. If no connections were generated, no cables will be generated.
