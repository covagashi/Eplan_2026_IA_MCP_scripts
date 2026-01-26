# DeviceTags(IFunctionBase[],String,DeviceTags,String,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1433.html

---

Method for numbering device tags in a project.

Syntax

**C#**



public void DeviceTags( 

   IFunctionBase[] pFunctions,

   string strFilterScheme,

   Renumber.Enums.DeviceTags eDeviceTagKind,

   string strScheme,

   int nStartValue,

   int nIncrement

)

public:

void DeviceTags( 

   array<IFunctionBase^>^ pFunctions,

   String^ strFilterScheme,

   Renumber.Enums.DeviceTags eDeviceTagKind,

   String^ strScheme,

   int nStartValue,

   int nIncrement

)


#### Parameters

*pFunctions*
:   IFunctionBase objects of which the device tags will be numbered.

*strFilterScheme*
:   Filter scheme. If an empty string is set in this parameter, the last\-used filter scheme will be used which is currently set in GUI. When `null` is passed no filter scheme is used.

*eDeviceTagKind*
:   Determines, which devices will be numbered.

*strScheme*
:   Numbering scheme.

*nStartValue*
:   Start value of the numbering.

*nIncrement*
:   Step width of the numbering.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for numbering could not be created. |
| **ApplicationException** | Thrown when renumber couldn't find any functions to renumber . |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
