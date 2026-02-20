# ExportAssignmentList Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ExportAssignmentList.html

---

Exports PLC assignment lists

Syntax

**C#**



public void ExportAssignmentList( 

   Project oProject,

   string strConfigurationProject,

   string strStation,

   string strCPU,

   string strLanguage,

   string strAssignmentListFileName

)

public:

void ExportAssignmentList( 

   Project^ oProject,

   String^ strConfigurationProject,

   String^ strStation,

   String^ strCPU,

   String^ strLanguage,

   String^ strAssignmentListFileName

)


#### Parameters

*oProject*
:   Project of which the PLC assignment list will be exported.

*strConfigurationProject*
:   PLC configuration project name or empty string. If you do not fill parameter strConfigurationProject you can only export i/o data which is related to plc boxes where the the configuration project also is empty.

*strStation*
:   PLC station name or empty string. If you do not not fill parameter strStation you can only export i/o data which is related to plc boxes where the station name also is empty.

*strCPU*
:   PLC CPU or empty string. If you do not fill parameter strCPU you can only export i/o data which is related to plc boxes where the cpu name also is empty.

*strLanguage*
:   Language shortcut to determine the export language, e.g. "en\_US".

*strAssignmentListFileName*
:   Alternative file name and path. If empty parameter will be taken from PLC scheme.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| **ApplicationException** | \Internal interface for exporting PLC data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |

Remarks

If no scheme name (strScheme) is passed, the last-used scheme will be used which is currently set in GUI. The file name of the export file is defined in the scheme.
