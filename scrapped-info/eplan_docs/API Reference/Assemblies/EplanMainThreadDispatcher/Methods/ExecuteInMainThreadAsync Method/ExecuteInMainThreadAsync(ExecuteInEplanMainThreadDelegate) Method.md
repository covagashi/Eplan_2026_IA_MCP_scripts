# ExecuteInMainThreadAsync(ExecuteInEplanMainThreadDelegate) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic8.html

---

Execute this work in a asynchronous main thread.

Syntax

**C#**



public void ExecuteInMainThreadAsync( 

   ExecuteInEplanMainThreadDelegate pExecuteDelegate

)

public:

void ExecuteInMainThreadAsync( 

   ExecuteInEplanMainThreadDelegate^ pExecuteDelegate

)


#### Parameters

*pExecuteDelegate*
:   The work to be done.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when no MainThreadDispatcher was set. |
