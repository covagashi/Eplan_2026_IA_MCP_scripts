# DeviceTagsWithPlcData(Function[],String,Boolean,DeviceTagsWithPLCOverwrition) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1434.html

---

Method for numbering device tags of a collection of functions with PLC data.

Syntax

**C#**



public void DeviceTagsWithPlcData( 

   Function[] pFunctions,

   string strScheme,

   bool bMarkAsNumeratedByPLC,

   Renumber.Enums.DeviceTagsWithPLCOverwrition eOverwriteMode

)

public:

void DeviceTagsWithPlcData( 

   array<Function^>^ pFunctions,

   String^ strScheme,

   bool bMarkAsNumeratedByPLC,

   Renumber.Enums.DeviceTagsWithPLCOverwrition eOverwriteMode

)


#### Parameters

*pFunctions*
:   Functions, for which the device tags will be numbered.

*strScheme*
:   Scheme used for numbering.

*bMarkAsNumeratedByPLC*
:   Mark as 'numbered with PLC data'.

*eOverwriteMode*
:   Overwrite mode. Use value from enum DeviceTagsWithPLCOverwrition.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown, if an argument is set to null. |
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified functions do not exist or are invalid. |
| **ApplicationException** | \Internal interface for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |
