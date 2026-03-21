# ReaddressTerminals(Project,String,String,String,String,String,String,String,Sorting) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1400.html

---

Executes PLC terminals addressing

Syntax

**C#**



public void ReaddressTerminals( 

   Project oProject,

   string strDigitalInputStartAddress,

   string strDigitalOutputStartAddress,

   string strAnalogInputStartAddress,

   string strAnalogOutputStartAddress,

   string strConfigurationProject,

   string strStation,

   string strCPU,

   PlcService.Sorting eSorting

)

public:

void ReaddressTerminals( 

   Project^ oProject,

   String^ strDigitalInputStartAddress,

   String^ strDigitalOutputStartAddress,

   String^ strAnalogInputStartAddress,

   String^ strAnalogOutputStartAddress,

   String^ strConfigurationProject,

   String^ strStation,

   String^ strCPU,

   PlcService.Sorting eSorting

)


#### Parameters

*oProject*
:   A project to perform re-addressing on.

*strDigitalInputStartAddress*
:   Start digital input address. Can be empty.

*strDigitalOutputStartAddress*
:   Start digital output address. Can be empty.

*strAnalogInputStartAddress*
:   Start analog input address. Can be empty.

*strAnalogOutputStartAddress*
:   Start analog output address. Can be empty.

*strConfigurationProject*
:   PLC configuration project name. Can be empty.

*strStation*
:   PLC station name. Can be empty.

*strCPU*
:   PLC CPU. Can be empty.

*eSorting*
:   Sorting method.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given Project does not exist or isn't valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the re-addressing process. |
