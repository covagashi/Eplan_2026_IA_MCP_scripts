# ExecuteInMainThreadAsync(ExecuteInEplanMainThreadDelegate1,Object) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic7.html

---

Execute this work in a asynchronous main thread.

Syntax

**C#**



public void ExecuteInMainThreadAsync( 

   ExecuteInEplanMainThreadDelegate1 pExecuteDelegate,

   object x

)

public:

void ExecuteInMainThreadAsync( 

   ExecuteInEplanMainThreadDelegate1^ pExecuteDelegate,

   Object^ x

)


#### Parameters

*pExecuteDelegate*
:   The work to be done.

*x*
:   Parameter 1 for the work delegate.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when no MainThreadDispatcher was set. |
