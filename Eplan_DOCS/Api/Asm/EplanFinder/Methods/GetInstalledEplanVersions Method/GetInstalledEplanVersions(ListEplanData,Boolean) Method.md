# GetInstalledEplanVersions(List<EplanData>,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.EplanFinder~GetInstalledEplanVersions(List{EplanData},Boolean).html

---

Get EPLAN versions which are currently installed on local machine.

Syntax

**C#**



public void GetInstalledEplanVersions( 

   ref List<EplanData> lEplanVersions,

   bool b64bit

)

public:

void GetInstalledEplanVersions( 

   List<EplanData>^% lEplanVersions,

   bool b64bit

)


#### Parameters

*lEplanVersions*
:   List to be filled with information about EPLAN versions currently installed on local machine.

*b64bit*
:   True - returns only 64 bit versions list. False - returns only 32-bit versions
