# EplAssert

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplAssert.html

---

The EplAssert class. When the advaced mode is activated in ELogFileConfigTool, Asserts are written to the epllog.txt Its also possible to activate a debugger break. Set the registry value User / Software / Eplan / Eplan W3 / Assert / BreakOnAssert to true, and the debugger will stop at a failed assert.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.EplAssert**

Syntax

**C#**



public class EplAssert

public ref class EplAssert


Example

Example of EplAssert:

**C#**

```
object testObject = null;

Eplan.EplApi.Base.EplAssert oAssert= new Eplan.EplApi.Base.EplAssert();

oAssert.Assert (testObject != null, "The testobject must not be null!");
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplAssert Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplAssert~_ctor.html) |  |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Assert](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplAssert~Assert.html) | A Delevoper Assertion. When the boolean Expression fails, the debugged application fails into the debugger. Some Text is written to the EplLog.txt |


