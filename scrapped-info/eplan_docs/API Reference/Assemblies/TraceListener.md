# TraceListener

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.TraceListener.html

---

Output of trace messages to the EPLAN system message management (incl. EPLAN log file)

Inheritance Hierarchy

[System.Object](#)  
   [System.MarshalByRefObject](#)  
      [System.Diagnostics.TraceListener](#)  
         **Eplan.EplApi.Base.TraceListener**

Syntax

**C#**



public class TraceListener : System.Diagnostics.TraceListener

public ref class TraceListener : public System.Diagnostics.TraceListener


Example

Example of TRACE outputs

**C#**

```
Eplan.EplApi.Base.TraceListener oTrace= new Eplan.EplApi.Base.TraceListener();

System.Diagnostics.Trace.Listeners.Add(oTrace); // When new trace listeners are created and added, they must be removed again later!

oTrace.WriteLine("Begin Execute"); // Only write to the EPLAN system message management.

System.Diagnostics.Trace.WriteLine("Begin Execute"); // Send to all trace listeners.

oTrace.Close();

System.Diagnostics.Trace.Listeners.Remove(oTrace);
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [TraceListener Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.TraceListener~_ctor.html) |  |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Attributes](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Property | [Filter](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Property | [IndentLevel](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Property | [IndentSize](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Property | [IsThreadSafe](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Property | [Name](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Property | [TraceOutputOptions](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Close](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [CreateObjRef](#) | (Inherited from [System.MarshalByRefObject](#)) |
| Public Method | [Dispose()](#) | Destructor for deterministic finalization of TraceListener object. (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [Fail](#) | Overloaded.  (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [Flush](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [GetLifetimeService](#) | (Inherited from [System.MarshalByRefObject](#)) |
| Public Method | [InitializeLifetimeService](#) | (Inherited from [System.MarshalByRefObject](#)) |
| Public Method | [TraceData](#) | Overloaded.  (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [TraceEvent](#) | Overloaded.  (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [TraceTransfer](#) | (Inherited from [System.Diagnostics.TraceListener](#)) |
| Public Method | [Write](Eplan.EplApi.Baseu~Eplan.EplApi.Base.TraceListener~Write.html) | Overloaded. Overridden. Outputs a line to the system message management. |
| Public Method | [WriteLine](Eplan.EplApi.Baseu~Eplan.EplApi.Base.TraceListener~WriteLine.html) | Overloaded. Overridden. Outputs a line to the system message management. |


