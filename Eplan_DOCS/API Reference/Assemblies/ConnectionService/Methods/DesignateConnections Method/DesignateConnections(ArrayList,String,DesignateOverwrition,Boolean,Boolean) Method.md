# DesignateConnections(ArrayList,String,DesignateOverwrition,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1320.html

---

Designate connections (wires) with connection definition point.

Syntax

**C#**



public void DesignateConnections( 

   Project oProject,

   string strSchemaName,

   ConnectionService.DesignateOverwrition rOverwriteMode,

   bool bMarkAsManual,

   bool bRegenrateConnections

)

public:

void DesignateConnections( 

   Project^ oProject,

   String^ strSchemaName,

   ConnectionService.DesignateOverwrition rOverwriteMode,

   bool bMarkAsManual,

   bool bRegenrateConnections

)


#### Parameters

*oProject*
:   Project in which the connections will be designated.

*strSchemaName*
:   Name of the scheme, which is used for the wire numbering.

*rOverwriteMode*
:   Mode to determine whether already existing connection designations will be overwritten. Valid values are\:0, 1, and See enum DESIGNATE\_OVERWRITE\_MODE.

*bMarkAsManual*
:   If this flag is set to true, the created connection designations will be marked as "manually set".

*bRegenrateConnections*
:   If set to true, connections in the project will be updated prior to running the connection designation.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | \Parameters contained invalid values. |
| **ApplicationException** | \Internal interface necessary for wire designation could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during wire designation. Pleas read the exception message. |
| **InvalidScheme** | An error occurs when used scheme name doesn't exist |

Remarks

If no scheme exists under the given scheme name (strSchemaName), an ArgumentException is thrown. If strSchemaName is set to an empty string, the last-used scheme will be used which is currently set in GUI. Unlike in the GUI, connections are not always generated, but only if bRegenrateConnections is set to true.
