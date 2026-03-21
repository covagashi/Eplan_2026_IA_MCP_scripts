# AlignAndFormatConnectionDefinitionPoints(ArrayList,String,Align,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1311.html

---

function to re-align and re-format connection definition points.

Syntax

**C#**



public void AlignAndFormatConnectionDefinitionPoints( 

   Project oProject,

   string strSchemaName,

   ConnectionService.Align rAlignFormatMode,

   bool bLeaveManuals,

   bool bRegenrateConnections

)

public:

void AlignAndFormatConnectionDefinitionPoints( 

   Project^ oProject,

   String^ strSchemaName,

   ConnectionService.Align rAlignFormatMode,

   bool bLeaveManuals,

   bool bRegenrateConnections

)


#### Parameters

*oProject*
:   Project in which to format and align connection definition points.

*strSchemaName*
:   Name of the scheme, which is used for wire numbering.

*rAlignFormatMode*
:   Mode, which will be used for aligning and formatting of connection definition points. The values 0, 1, and 2 are allowed. See enum [ConnectionService.Align](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService+Align.html) .

*bLeaveManuals*
:   If set to true, connection definition points indicated as 'manually set' are ignored.

*bRegenrateConnections*
:   If set to true, connections will be generated before formatting.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Invalid parameters found. |
| **ApplicationException** | A necessary internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during formatting the connection definition points. |
| **InvalidScheme** | An error occurs when used scheme name doesn't exist |

Remarks

If no scheme exists under the given scheme name (strSchemaName), an ArgumentException is thrown. If strSchemaName is set to an empty string, the last-used scheme will be used which is currently set in GUI. Unlike in the GUI, connections are not always generated, but only if bRegenrateConnections is set to true.
