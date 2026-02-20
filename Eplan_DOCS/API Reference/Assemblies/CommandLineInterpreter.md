# CommandLineInterpreter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter.html

---

Class for executing commands in command-line style

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.CommandLineInterpreter**

Syntax

**C#**



[ClassInterface(ClassInterfaceType.None)]

public class CommandLineInterpreter : ICommandLineInterpreter

[ClassInterface(ClassInterfaceType.None)]

public ref class CommandLineInterpreter : public ICommandLineInterpreter


Example

Example of executing command-line commands

**C#**

```
String strAction= @"XPrjActionProjectOpen /PROJECT:";

bool bRet= CommandLineInterpreter().Execute(strAction + ProjectName);

if (!bRet)

{

   new Decider().Decide(EnumDecisionType.eOkDecision, "P8 command does not work", "OpenProjectAndPage", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

   CommandLineInterpreter.Execute("SystemErrDialog");

   return -1;

}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [CommandLineInterpreter Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~_ctor.html) | Overloaded. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Execute](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~Execute.html) | Overloaded. Execution of a command |
| Public Method | [IsExecutable](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.CommandLineInterpreter~IsExecutable.html) | Checks whether the execution of an expression is possible.  This is only the case when the corresponding action is available. |


