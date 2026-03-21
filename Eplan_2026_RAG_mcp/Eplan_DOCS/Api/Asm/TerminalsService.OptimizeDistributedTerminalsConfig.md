# TerminalsService.OptimizeDistributedTerminalsConfig

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService+OptimizeDistributedTerminalsConfig.html

---

Options for optimizing distributed terminals.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.HEServices.TerminalsService.OptimizeDistributedTerminalsConfig**

Syntax

**C#**



public class TerminalsService.OptimizeDistributedTerminalsConfig

public ref class TerminalsService.OptimizeDistributedTerminalsConfig

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [TerminalsService.OptimizeDistributedTerminalsConfig Constructor](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService+OptimizeDistributedTerminalsConfig~_ctor.html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [FunctionDefinitionGroup](topic1453.html) | An integer specifying a default [Eplan.EplApi.DataModel.FunctionDefinition.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Group.html) for distributed terminals. If part number of a distributed terminal is empty, the distributed terminal will get the specified function definition group. The default is 10. |
| Public Property | [KeepConnPointDesignations](topic1454.html) | If TRUE, the connection points will keep their designations. If FALSE, the connection points with designations will be treated like connection points without designations. Default is TRUE. |
| Public Property | [KeepDesignations](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService+OptimizeDistributedTerminalsConfig~KeepDesignations.html) | If TRUE, the distributed terminals will keep their device tag. If FALSE, the distributed terminals with device tag will be treated like distributed terminals without device tag. Default is TRUE. |
| Public Property | [PartNumberTerminal](topic1455.html) | Part number that the distributed main terminal with 'Normal' potential will get. If the part contains a function definition, this function definition will be the new function definition of the terminal. By default, this option is empty. |
| Public Property | [PartNumberTerminalN](topic1456.html) | Part number that the distributed main terminal with 'N' potential will get. If the part contains a function definition, this function definition will be the new function definition of the terminal. By default, this option is empty. |
| Public Property | [PartNumberTerminalPE](topic1457.html) | Part number that the distributed main terminal with 'PE' potential will get. If the part contains a function definition, this function definition will be the new function definition of the terminal. By default, this option is empty. |
| Public Property | [PartNumberTerminalSH](topic1458.html) | Part number that the distributed main terminal with 'SH' potential will get. If the part contains a function definition, this function definition will be the new function definition of the terminal. By default, this option is empty. |
| Public Property | [UniteConnected](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService+OptimizeDistributedTerminalsConfig~UniteConnected.html) | If TRUE, connected distributed terminals will be sorted on the strip, so that they are located together on the strip. Default is TRUE. |
| Public Property | [UniteConnectedPE](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.TerminalsService+OptimizeDistributedTerminalsConfig~UniteConnectedPE.html) | If TRUE, connected distributed PE-terminals will be sorted on the strip, so that they are located together on the strip. Default is TRUE. |


