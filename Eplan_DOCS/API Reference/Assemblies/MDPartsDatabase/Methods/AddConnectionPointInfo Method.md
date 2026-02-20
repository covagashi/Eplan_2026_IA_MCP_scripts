# AddConnectionPointInfo Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~AddConnectionPointInfo.html

---

Adds a new connection point info to the parts data

Syntax

**C#**



public MDConnectionPointInfo AddConnectionPointInfo( 

   string name

)

public:

MDConnectionPointInfo^ AddConnectionPointInfo( 

   String^ name

)


#### Parameters

*name*
:   The name of the connection point info will be added.

Exceptions

| Exception | Description |
| --- | --- |
|  | If connection point info already exists. |

Remarks

The name has to be unique in the connection point info list of the parts database.
