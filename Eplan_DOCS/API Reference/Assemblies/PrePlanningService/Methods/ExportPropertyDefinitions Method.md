# ExportPropertyDefinitions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~ExportPropertyDefinitions.html

---

Exports all user defined properties from project to file. Properties identified as "Do not use anymore" will not be exported.

Syntax

**C#**



public bool ExportPropertyDefinitions( 

   Project pProject,

   string strFileName

)

public:

bool ExportPropertyDefinitions( 

   Project^ pProject,

   String^ strFileName

)


#### Parameters

*pProject*
:   Project from which all user defined properties are exported. Can't be `null`.

*strFileName*
:   Full file name of target file. Can't be `null` or `empty`.

#### Return Value

Returns `true` if export is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pProject` is a `null` value. |
| [System.ArgumentException](#) | Thrown when `strFileName` of `null` or `empty`. |
