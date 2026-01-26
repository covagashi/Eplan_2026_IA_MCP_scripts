# ImportAssignmentList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ImportAssignmentList.html

---

Imports PLC assignment lists.

Syntax

**C#**



public void ImportAssignmentList( 

   Project oProject,

   string strConfigurationProject,

   string strStation,

   string strCPU,

   string strLanguage,

   string strAssignmentListFileName,

   bool bCompByAddress,

   bool bAcceptInvAddr

)

public:

void ImportAssignmentList( 

   Project^ oProject,

   String^ strConfigurationProject,

   String^ strStation,

   String^ strCPU,

   String^ strLanguage,

   String^ strAssignmentListFileName,

   bool bCompByAddress,

   bool bAcceptInvAddr

)


#### Parameters

*oProject*
:   Project into which the PLC assignment list will be imported.

*strConfigurationProject*
:   PLC configuration project name

*strStation*
:   PLC station name

*strCPU*
:   PLC CPU.

*strLanguage*
:   Language shortcut for the import, e.g. "en\_US".

*strAssignmentListFileName*
:   Alternative file name and path. If empty parameter will be taken from PLC scheme.

*bCompByAddress*
:   If set to true, the PLC address is used as reference value.

*bAcceptInvAddr*
:   If set to true, even invalid addresses will be read.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for importing PLC data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. |

Remarks

If no scheme name (strScheme) is passed, the last-used scheme will be used which is currently set in GUI. The name of the file to import is defined in the scheme.
