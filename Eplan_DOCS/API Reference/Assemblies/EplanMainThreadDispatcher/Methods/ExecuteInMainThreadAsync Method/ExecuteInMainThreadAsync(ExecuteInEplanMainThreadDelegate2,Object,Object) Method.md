# ExecuteInMainThreadAsync(ExecuteInEplanMainThreadDelegate2,Object,Object) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic6.html

---

Execute this work in a asynchronous main thread.

Syntax

**C#**



public void ExecuteInMainThreadAsync( 

   ExecuteInEplanMainThreadDelegate2 pExecuteDelegate,

   object x,

   object y

)

public:

void ExecuteInMainThreadAsync( 

   ExecuteInEplanMainThreadDelegate2^ pExecuteDelegate,

   Object^ x,

   Object^ y

)


#### Parameters

*pExecuteDelegate*
:   The work to be done.

*x*
:   Parameter 1 for the work delegate.

*y*
:   Parameter 2 for the work delegate.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when no MainThreadDispatcher was set. |
