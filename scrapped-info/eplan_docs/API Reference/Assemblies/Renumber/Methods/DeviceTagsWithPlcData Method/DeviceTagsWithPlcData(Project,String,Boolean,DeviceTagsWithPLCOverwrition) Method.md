# DeviceTagsWithPlcData(Project,String,Boolean,DeviceTagsWithPLCOverwrition) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1435.html

---

Method for numbering device tags of a project with PLC data.

Syntax

**C#**



public void DeviceTagsWithPlcData( 

   Project pProject,

   string strScheme,

   bool bMarkAsNumeratedByPLC,

   Renumber.Enums.DeviceTagsWithPLCOverwrition eOverwriteMode

)

public:

void DeviceTagsWithPlcData( 

   Project^ pProject,

   String^ strScheme,

   bool bMarkAsNumeratedByPLC,

   Renumber.Enums.DeviceTagsWithPLCOverwrition eOverwriteMode

)


#### Parameters

*pProject*
:   Project in which the device tags will be numbered.

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
| **ArgumentException** | Thrown in case of invalid parameters, e.g. the specified project does not exist or is invalid. |
| **ApplicationException** | \Internal interface for numbering could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during numbering. |
| **InvalidScheme** | An error occurrs when used scheme name doesn't exist |
