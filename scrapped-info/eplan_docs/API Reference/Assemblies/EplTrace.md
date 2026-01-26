# EplTrace

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace.html

---

Trace the output to the EplLog.txt file. This Trace class works in debug and release mode, while the trace listener works only in debug mode. Traces are written when the registry key HKCU / Software / Eplan / Eplan W3 / Trace / \-ModuleName- is found.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.EplTrace**

Syntax

**C#**



public class EplTrace

public ref class EplTrace


Example

Example of TRACE outputs

- [c#](#i-tab-content-a39980c1-5d3b-4dd0-b51c-8d33aa3d72d9)

```
Eplan.EplApi.Base.EplTrace oTrace= new Eplan.EplApi.Base.EplTrace();

oTrace.Trace ("Eplan.EplApi.Base", "Start executing function abc");
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplTrace Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace~_ctor.html) |  |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Trace](Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace~Trace.html) | Overloaded. Writes the text to EplLog.txt when Trace is on. |


