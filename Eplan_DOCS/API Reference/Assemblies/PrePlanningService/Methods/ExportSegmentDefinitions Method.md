# ExportSegmentDefinitions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~ExportSegmentDefinitions.html

---

Exports all segment definitions from project to file.

Syntax

**C#**



public bool ExportSegmentDefinitions( 

   Project pProject,

   string strFileName

)

public:

bool ExportSegmentDefinitions( 

   Project^ pProject,

   String^ strFileName

)


#### Parameters

*pProject*
:   Project from which all segment definitions are exported. Can't be `null`.

*strFileName*
:   Full file name of target file. Can't be `null` or `empty`.

#### Return Value

Returns `true` if export is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pProject` is a `null` value. |
| [System.ArgumentException](#) | Thrown when `strFileName` of `null` or `empty`. |
