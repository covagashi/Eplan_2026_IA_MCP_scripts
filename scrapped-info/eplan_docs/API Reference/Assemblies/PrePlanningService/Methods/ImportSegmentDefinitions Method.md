# ImportSegmentDefinitions Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~ImportSegmentDefinitions.html

---

Imports segment definitions from file to project.

Syntax

**C#**



public bool ImportSegmentDefinitions( 

   Project pProject,

   string strFileName

)

public:

bool ImportSegmentDefinitions( 

   Project^ pProject,

   String^ strFileName

)


#### Parameters

*pProject*
:   Project to which segment definitions are exported. Can't be `null`.

*strFileName*
:   Full file name of source file. Can't be `null` or `empty`.

#### Return Value

Returns `true` if import is successful.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pProject` is a `null` value. |
| [System.ArgumentException](#) | Thrown when `strFileName` of `null` or `empty`. |
