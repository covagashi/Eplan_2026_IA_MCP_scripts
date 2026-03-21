# EplanMainThreadDispatcher

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher.html

---

EplanMainThreadDispatcher can execute some work in the main thread of Eplan.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher**

Syntax

**C#**



public class EplanMainThreadDispatcher

public ref class EplanMainThreadDispatcher


Remarks

Executing API code purely of of main Eplan thread is not recommended, i.e. such scenarios were not tested and are out of support. So the class enables executing API code on a main thread from another thread (i.e. like in case of non-modal dialogs or a background worked)

Example

**C#**

```


//run an action asynchronously e.g from DoWork event handler of BackgroundWorker

eplanMainThreadDispatcher.ExecuteInMainThreadAsync(

        () => { new CommandLineInterpreter().Execute("check /TYPE:PROJECT"); }

    );

//create a progress bar with a background work

using (Progress progress = new Progress("SimpleProgress"))

{

    eplanMainThreadDispatcher.AddProgressBackgroundWork(progress,

        () => { new CommandLineInterpreter().Execute("check /TYPE:PROJECT"); }

    );

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [EplanMainThreadDispatcher Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~_ctor.html) | Creates a new dispatcher |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddProgressBackgroundWork](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~AddProgressBackgroundWork.html) | Allows the user to add a progress bar when main thread is working. |
| Public Methodstatic (Shared in Visual Basic) | [CanAccessMainThread](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~CanAccessMainThread.html) | Allows the user to access the main thread both synchronously and asynchronously. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~Dispose().html) | Destructor for deterministic finalization of EplanMainThreadDispatcher object. |
| Public Method | [ExecuteInMainThreadAsync](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~ExecuteInMainThreadAsync.html) | Overloaded. Execute this work in a asynchronous main thread. |
| Public Method | [ExecuteInMainThreadSync](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~ExecuteInMainThreadSync.html) | Execute this work in a synchronous main thread. |
| Public Methodstatic (Shared in Visual Basic) | [GetMainThreadDispatcher](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~GetMainThreadDispatcher.html) | Allows to use the dispatcher to work on synchronous and asynchronous threads. |


