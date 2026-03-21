# GetPLCConfigurationProjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~GetPLCConfigurationProjects.html

---

Returns a list of PLC config. projects included in the EPLAN P8's project.

Syntax

**C#**



public string[] GetPLCConfigurationProjects( 

   Project oProject

)

public:

array<String^>^ GetPLCConfigurationProjects( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project to get the list of PLC config. projects from.

Remarks

These names may be used as values of strConfigurationProject parameter of the ExportData method.
