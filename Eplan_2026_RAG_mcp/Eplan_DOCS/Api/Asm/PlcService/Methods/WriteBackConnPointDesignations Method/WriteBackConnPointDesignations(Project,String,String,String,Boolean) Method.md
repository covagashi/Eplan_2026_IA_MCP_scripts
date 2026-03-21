# WriteBackConnPointDesignations(Project,String,String,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1401.html

---

Writes back connection point designations from the overview PLC terminals of the given CPU to associated schematic PLC terminals.

Syntax

**C#**



public Function[] WriteBackConnPointDesignations( 

   Project prj,

   string sConfigurationsProjectName,

   string sStationName,

   string sCPUName,

   bool bAlsoToConnectedPlugsAndTerminals

)

public:

array<Function^>^ WriteBackConnPointDesignations( 

   Project^ prj,

   String^ sConfigurationsProjectName,

   String^ sStationName,

   String^ sCPUName,

   bool bAlsoToConnectedPlugsAndTerminals

)


#### Parameters

*prj*
:   A project to perform the action in.

*sConfigurationsProjectName*
:   PLC configuration project name.

*sStationName*
:   PLC station name.

*sCPUName*
:   A CPU name.

*bAlsoToConnectedPlugsAndTerminals*
:   Specifies whether the directly connected plugs / terminals should also be affected.

#### Return Value

An array of functions (PLC terminals, terminals, plugs) affected by the operation.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the given project does not exist or isn't valid. |
| **NOPLCCPU** | An error occurrs when no PLC CPU found in the project |

Remarks

'¢ The terminals must have a CPU name specified.  
'¢ The method corresponds to the "Write back connection point designations" dialog in P8.  
'¢ This functionality has been moved within the GUI: Up to version 2.8, it could be found under "Project Data" > "PLC" > "Write back connection point designations...". Since version 2.9, it is part of the project correction scheme in the GUI.
