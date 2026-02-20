# Creating add-ins in Visual Basic .NET

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/VisualBasicAddins.html

---

Writing an add-in in Visual Basic .NET is basically the same as described in the topic "[Creating add-ins in CSharp](CSharpAddins.html)". The only difference is the source code syntax and the way the compiler is called.

Create a "VBAddInModule.vb" file with the following content:

```vb
Public Class AddInModule
    Implements Eplan.EplApi.ApplicationFramework.IEplAddIn
 
    Public Function OnRegister(ByRef bLoadOnStart As System.Boolean) As Boolean _
      Implements Eplan.EplApi.ApplicationFramework.IEplAddIn.OnRegister
       bLoadOnStart = True
       Return True
    End Function 'OnRegister
 
    Public Function OnUnregister() As Boolean _
     Implements Eplan.EplApi.ApplicationFramework.IEplAddIn.OnUnregister
       Return True
    End Function 'OnUnregister
 
    Public Function OnInit() As Boolean _
     Implements Eplan.EplApi.ApplicationFramework.IEplAddIn.OnInit
       Return True
    End Function 'OnInit
 
    Public Function OnInitGui() As Boolean _
     Implements Eplan.EplApi.ApplicationFramework.IEplAddIn.OnInitGui
       Return True
    End Function 'OnInitGui
 
    Public Function OnExit() As Boolean _
     Implements Eplan.EplApi.ApplicationFramework.IEplAddIn.OnExit
       Return True
    End Function 'OnExit
 End Class 'AddInModule
```

Invoke the Visual Basic compiler (vbc.exe) with the following parameters:

vbc /target:library /reference:..\..\..\..\bin\Eplan.EplApi.AFu.dll /out:SimpleVBAddIn.dll VBAddinModule.vb 

For an action create the following source file and save it as "SimpleVBAction.cs" in your source directory. To create an action, we need a class that implements the  IEplAction  interface. For a more detailed explanation, see the "[Actions](Actions.html)" topic.

```vb
Imports Eplan.EplApi.ApplicationFramework
 
 Public Class VBAction
    Implements IEplAction
    Public Function Execute(ctx As ActionCallingContext) As Boolean Implements IEplAction.Execute
       Dim dec As Decider = New Decider
       dec.Decide(EnumDecisionType.eOkDecision, "VBAction was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
       Return True
    End Function 'Execute
 
    Public Function OnRegister(ByRef Name As String, ByRef Ordinal As Integer) As Boolean _
     Implements IEplAction.OnRegister
       Name = "VBAction"
       Ordinal = 20
       Return True
    End Function 'OnRegister
 
    Public Sub GetActionProperties(ByRef actionProperties As ActionProperties) _
     Implements IEplAction.GetActionProperties
    End Sub 'GetActionProperties
 End Class 'VBAction
```

vbc /target:library /reference:..\..\..\..\bin\Eplan.EplApi.AFu.dll /reference:..\..\..\..\bin\Eplan.EplApi.Baseu.dll /out:SimpleVBAddIn.dll VBAddinModule.vb SimpleVBAction.vb