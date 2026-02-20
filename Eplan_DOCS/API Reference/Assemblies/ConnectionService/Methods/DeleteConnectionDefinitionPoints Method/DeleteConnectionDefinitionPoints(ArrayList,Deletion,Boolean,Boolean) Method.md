# DeleteConnectionDefinitionPoints(ArrayList,Deletion,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1315.html

---

Delete wire designations and connection definition points. This method acts only on connection definition points associated with (i.e. returned by) a connection existing in the project

Syntax

**C#**



public void DeleteConnectionDefinitionPoints( 

   Project oProject,

   ConnectionService.Deletion rDeleteMode,

   bool bLeaveManuals,

   bool bRegenrateConnections

)

public:

void DeleteConnectionDefinitionPoints( 

   Project^ oProject,

   ConnectionService.Deletion rDeleteMode,

   bool bLeaveManuals,

   bool bRegenrateConnections

)


#### Parameters

*oProject*
:   Project in which to delete the wire designations or connection definition points.

*rDeleteMode*
:   Delete mode. Valid values are 0 and 1. See enumeration [ConnectionService.Deletion](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService+Deletion.html).

*bLeaveManuals*
:   If set to true, connection definition points indicated as 'manually set' are ignored.

*bRegenrateConnections*
:   If set to true, first the connections will be regenerated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | An internal interface necessary for the function could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred, while deleting connection definition points or wire designations. Please read the exception message |
| **InvalidScheme** | An error occurs when used scheme name doesn't exist |

Remarks

The last-used scheme which is currently set in GUI will be used during the operation. Unlike in the GUI, connections are not always generated, but only if bRegenrateConnections is set to true. CDPs to remove are taken from Connection.ConnectionDefPoints property. This property is updated after generating connections. Some methods like Cable.Create or Cable.SetLogicalArea don't update connections and Connection.ConnectionDefPoints property is empty which causes that CDP will not be removed. Please make sure that connections are up-to-date before using this method or use it with parameter bRegenerateConnections set to true.
