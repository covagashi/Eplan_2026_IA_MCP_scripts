# ExportAddressOverview Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~ExportAddressOverview.html

---

Exports PLC address overview list into csv file.

Syntax

**C#**



public void ExportAddressOverview( 

   Project oProject,

   string strPlcConfigurationProject,

   string strPlcStation,

   string strPlcCpu,

   string strAddressOverviewFileName

)

public:

void ExportAddressOverview( 

   Project^ oProject,

   String^ strPlcConfigurationProject,

   String^ strPlcStation,

   String^ strPlcCpu,

   String^ strAddressOverviewFileName

)


#### Parameters

*oProject*
:   Project of which the PLC address overview list will be exported.

*strPlcConfigurationProject*
:   PLC configuration project name or empty string. If you do not fill parameter strConfigurationProject you can only export i/o data which is related to plc boxes where the the configuration project also is empty.

*strPlcStation*
:   PLC station name or empty string. If you do not not fill parameter strStation you can only export i/o data which is related to plc boxes where the station name also is empty.

*strPlcCpu*
:   PLC CPU or empty string. If you do not fill parameter strCPU you can only export i/o data which is related to plc boxes where the cpu name also is empty.

*strAddressOverviewFileName*
:   Alternative file name and path. If empty parameter will be taken from PLC scheme.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the export. |
