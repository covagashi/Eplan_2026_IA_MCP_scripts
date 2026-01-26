# Trace output

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/TraceOutput.html

---

For debugging purposes (or program logging in the release version) it is useful to log messages to a trace listener. The API framework provides a  TraceListener  class for this purpose.

In your API program, you simply add your own trace listener to the  System.Diagnostics.Trace.Listeners:

**C#**
```csharp
private Eplan.EplApi.Base.TraceListener m_oTrace;

//.

//.

//.

    m_oTrace= new Eplan.EplApi.Base.TraceListener();

//.

//.

//.

public bool Execute(ActionCallingContext ctx )

{

    System.Diagnostics.Trace.Listeners.Add(m_oTrace);

    System.Diagnostics.Trace.WriteLine(" Begin Execute ");

//.

//.

}

   m_oTrace= New Eplan.EplApi.Base.TraceListener()

    System.Diagnostics.Trace.Listeners.Add(m_oTrace)

    System.Diagnostics.Trace.WriteLine(" Begin Execute ")
```

As a result, all further trace outputs are visible in the Windows trace management and ' as the case may be ' written to the Eplan log database at the end of the program.

```


TRACE: .\Actions\AfCommandLineInterpreter.cpp(18) : AfCommandLineInterpreter::execute: CSharpAction

TRACE: .\Actions\AfAction.cpp(123) : Execute Action: URCheckRightsForAction

TRACE: .\Actions\AfAction.cpp(123) : Execute Action: CSharpAction

TRACE: u:\eplanw3_1.0_vc7.1\eplan\extensions\api_demosfue\v_1.0\eplan.w3addin.demo1\csharpaction.cs(24) : Begin Execute

```