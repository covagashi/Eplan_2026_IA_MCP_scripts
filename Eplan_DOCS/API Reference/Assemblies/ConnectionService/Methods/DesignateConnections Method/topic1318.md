# DesignateConnections(String,String,DesignateOverwrition,Boolean,Boolean,AvoidIdenticalDesignations,Visibility,Int32[],Int32[],Boolean[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1318.html

---

Designate connections (wires) with connection definition point.

Syntax

**C#**



public void DesignateConnections( 

   ArrayList arrConnectionList,

   string strSchemaName,

   ConnectionService.DesignateOverwrition rOverwriteMode,

   bool bMarkAsManual,

   bool bRegenrateConnections,

   ConnectionService.AvoidIdenticalDesignations avoidIdenticalDesignationsKind,

   ConnectionService.Visibility visibilityKind,

   int[] nStartValues,

   int[] nIncrements,

   bool[] bGroup

)

public:

void DesignateConnections( 

   ArrayList^ arrConnectionList,

   String^ strSchemaName,

   ConnectionService.DesignateOverwrition rOverwriteMode,

   bool bMarkAsManual,

   bool bRegenrateConnections,

   ConnectionService.AvoidIdenticalDesignations avoidIdenticalDesignationsKind,

   ConnectionService.Visibility visibilityKind,

   array<int>^ nStartValues,

   array<int>^ nIncrements,

   array<bool>^ bGroup

)


#### Parameters

*arrConnectionList*
:   List of connections for which the connections will be designated.

*strSchemaName*
:   Name of the scheme, which is used for the wire numbering.

*rOverwriteMode*
:   Mode to determine whether already existing connection designations will be overwritten. Valid values are\:0, 1, and See enum DESIGNATE\_OVERWRITE\_MODE.

*bMarkAsManual*
:   If this flag is set to true, the created connection designations will be marked as "manually set".

*bRegenrateConnections*
:   If set to true and arrConnectionList is not empty, connections in the project will be updated prior to running the connection designation.

*avoidIdenticalDesignationsKind*
:   Mode to avoid multiple designations(0 = None, 1 = In selection, 2 = In whole project, 3 = In each reset-range).

*visibilityKind*
:   Mode to change visibility of designations(0 = Do not change, 1 = All visible, 2 = Visible once per page and extent) .

*nStartValues*
:   Start-values for all defined counters and subcounters in scheme.

*nIncrements*
:   Step-values for all defined counters and subcounters in scheme.

*bGroup*
:   Group all defined counters and subcounters in scheme.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | \Parameters contained invalid values. |
| **ApplicationException** | \Internal interface necessary for wire designation could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during wire designation. Pleas read the exception message. |
| **InvalidScheme** | An error occurs when used scheme name doesn't exist |

Remarks

If no scheme exists under the given scheme name (strSchemaName), an ArgumentException is thrown. If strSchemaName is set to an empty string, the last-used scheme will be used which is currently set in GUI. Unlike in the GUI, connections are not always generated, but only if bRegenrateConnections is set to true.
