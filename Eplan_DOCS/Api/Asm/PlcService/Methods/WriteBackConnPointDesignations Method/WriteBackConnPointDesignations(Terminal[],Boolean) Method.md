# WriteBackConnPointDesignations(Terminal[],Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~WriteBackConnPointDesignations(Terminal[],Boolean).html

---

Writes back connection point designations from the selected overview PLC terminals to associated schematic PLC terminals.

Syntax

**C#**



public Function[] WriteBackConnPointDesignations( 

   Terminal[] arrPLCTerminals,

   bool bAlsoToConnectedPlugsAndTerminals

)

public:

array<Function^>^ WriteBackConnPointDesignations( 

   array<Terminal^>^ arrPLCTerminals,

   bool bAlsoToConnectedPlugsAndTerminals

)


#### Parameters

*arrPLCTerminals*
:   Selected overview PLC terminals.

*bAlsoToConnectedPlugsAndTerminals*
:   Specifies whether the directly connected plugs / terminals should also be affected.

#### Return Value

An array of functions (PLC terminals, terminals, plugs) affected by the operation.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing parameters. |
| **ArgumentException** | Thrown in case of invalid parameters. |

Remarks

'¢ The terminals must have a CPU name specified.  
'¢ The method corresponds to the "Write back connection point designations" dialog in P8.  
'¢ This functionality has been moved within the GUI: Up to version 2.8, it could be found under "Project Data" > "PLC" > "Write back connection point designations...". Since version 2.9, it is part of the project correction scheme in the GUI.
