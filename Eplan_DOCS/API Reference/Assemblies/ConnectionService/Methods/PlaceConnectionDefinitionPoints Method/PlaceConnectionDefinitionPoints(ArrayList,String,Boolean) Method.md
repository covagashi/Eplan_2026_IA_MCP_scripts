# PlaceConnectionDefinitionPoints(ArrayList,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1324.html

---

Function for placing connection definition points.

Syntax

**C#**



public void PlaceConnectionDefinitionPoints( 

   Project oProject,

   string strSchemaName,

   bool bRegenrateConnections

)

public:

void PlaceConnectionDefinitionPoints( 

   Project^ oProject,

   String^ strSchemaName,

   bool bRegenrateConnections

)


#### Parameters

*oProject*
:   Project in which the connection definition points will be placed.

*strSchemaName*
:   Name of the scheme used for placing connection definition points.

*bRegenrateConnections*
:   If set to true, connections will be regenerated prior to placing connection definition points.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | \Internal interface necessary for wire numbering functionality, could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred while placing connection definition points. |

Remarks

If no scheme exists under the given scheme name (strSchemaName), an ArgumentException is thrown. If strSchemaName is set to an empty string, the last-used scheme will be used which is currently set in GUI. Unlike in the GUI, connections are not always generated, but only if bRegenrateConnections is set to true. So when bRegenrateConnections is false, it is possible that connection definition points will be placed on wrong (i.e. old) positions or existing ones will not be recognized.
