# GetInstalledEplanVersions(List<EplanData>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanFinder~GetInstalledEplanVersions(List{EplanData}).html

---

Get EPLAN versions which are currently installed on local machine.

Syntax

**C#**



public void GetInstalledEplanVersions( 

   ref List<EplanData> lEplanVersions

)

public:

void GetInstalledEplanVersions( 

   List<EplanData>^% lEplanVersions

)


#### Parameters

*lEplanVersions*
:   List to be filled with information about EPLAN versions currently installed on local machine.

Remarks

Looks for 32 bit installations only
