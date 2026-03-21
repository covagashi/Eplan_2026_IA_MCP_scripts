# GetConnectionPointInfo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~GetConnectionPointInfo.html

---

Gets a connection point info with the given name that is stored in the parts database.

Syntax

**C#**



public MDConnectionPointInfo GetConnectionPointInfo( 

   string sName

)

public:

MDConnectionPointInfo^ GetConnectionPointInfo( 

   String^ sName

)


#### Parameters

*sName*
:   The name of the connection point info that is searched.

Remarks

Returns the found connection point info (MDConnectionPointInfo object) - otherwise null, if the connection point info is not found.
