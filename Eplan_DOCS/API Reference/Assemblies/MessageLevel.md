# MessageLevel

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.MessageLevel.html

---

Severity of the error

Syntax

**C#**



public enum MessageLevel : System.Enum

public enum class MessageLevel : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Assert** | 3 | Assert: The lowest level of an error, which will not appear in GUI. See also EplAssert class. |
| **Error** | 4 | Error |
| **FatalError** | 5 | Fatal Error |
| **Message** | 1 | Note |
| **Trace** | 0 | Trace: Trace message for developers. It will appear in the EplLog file, if "Advanced mode" is activated. |
| **Warning** | 2 | Warning |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.Base.MessageLevel**
