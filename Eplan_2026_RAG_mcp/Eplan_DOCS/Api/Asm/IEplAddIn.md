# IEplAddIn

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn.html

---

Interface declaration for an Eplan add-in. If an assembly is to be loaded as an Eplan add-in, exactly one class of the assembly must implement this interface.

Syntax

**C#**



[Guid("772B6E84-84D0-3597-8397-363C01BB41B6")]

public interface IEplAddIn

[Guid("772B6E84-84D0-3597-8397-363C01BB41B6")]

public interface class IEplAddIn

Public Methods

|  | Name | Description |
| --- | --- | --- |
| Method | [OnExit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnExit.html) | Is called at system shutdown if the add-in was loaded at system startup! |
| Method | [OnInit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnInit.html) | Is called if the add-in is to be loaded at system start-up. |
| Method | [OnInitGui](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnInitGui.html) | Called by the framework if the user interface was initialized and the add-in can modify the user interface. Is only called if the add-in is loaded at system startup! |
| Method | [OnRegister](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnRegister.html) | Is called once when a new add-in is selected. |
| Method | [OnUnregister](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnUnregister.html) | Is called once, when the add-in is removed from the system. |


