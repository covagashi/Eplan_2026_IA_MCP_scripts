# ExportProductionWiring(Project,PWMachineType,String,String,String,Language,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1323.html

---

Function for placing connection definition points (CDPs).

Syntax

**C#**



public void PlaceConnectionDefinitionPoints( 

   ArrayList arrConnectionList,

   string strSchemaName,

   bool bRegenrateConnections

)

public:

void PlaceConnectionDefinitionPoints( 

   ArrayList^ arrConnectionList,

   String^ strSchemaName,

   bool bRegenrateConnections

)


#### Parameters

*arrConnectionList*
:   List of connections on which the CDPs will be placed.

*strSchemaName*
:   Name of the scheme used for placing CDPs.

*bRegenrateConnections*
:   If set to true, connections will be regenerated prior to placing CDPs.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | \Internal interface necessary for wire numbering functionality, could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while placing CDPs. |
| **InvalidScheme** | An error occurs when used scheme name doesn't exist |

Remarks

If no scheme exists under the given scheme name (strSchemaName), an ArgumentException is thrown. If strSchemaName is set to an empty string, the last-used scheme will be used which is currently set in GUI. Unlike in the GUI, connections are not always generated, but only if bRegenrateConnections is set to true. So when bRegenrateConnections is false, it is possible that connection definition points will be placed on wrong (i.e. old) positions or existing ones will not be recognized.
