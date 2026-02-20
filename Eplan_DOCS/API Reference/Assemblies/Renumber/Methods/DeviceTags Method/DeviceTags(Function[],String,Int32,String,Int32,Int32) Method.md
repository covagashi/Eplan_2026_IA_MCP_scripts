# DeviceTags(Function[],String,Int32,String,Int32,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber~DeviceTags(Function[],String,Int32,String,Int32,Int32).html

---

Method for numbering device tags in a project.

Syntax

**C#**



public void DeviceTags( 

   Function[] pFunctions,

   string strFilterScheme,

   int eDeviceTagKind,

   string strScheme,

   int nStartValuePerIdentifier,

   int nIncrementPerIdentifier

)

public:

void DeviceTags( 

   array<Function^>^ pFunctions,

   String^ strFilterScheme,

   int eDeviceTagKind,

   String^ strScheme,

   int nStartValuePerIdentifier,

   int nIncrementPerIdentifier

)


#### Parameters

*pFunctions*
:   Functions of which the device tags will be numbered.

*strFilterScheme*
:   Filter scheme. If an empty string is set in this parameter, the last\-used filter scheme will be used which is currently set in GUI. When `null` is passed no filter scheme is used.

*eDeviceTagKind*
:   Determines, which devices will be numbered. Use value from enum DeviceTags.

*strScheme*
:   Numbering scheme.

*nStartValuePerIdentifier*
:   Start value of the numbering per identifier.

*nIncrementPerIdentifier*
:   Step width of the numbering per identifier.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for numbering could not be created. |
| **ApplicationException** | Thrown when renumber couldn't find any functions to renumber . |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |
