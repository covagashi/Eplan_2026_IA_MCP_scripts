# ExecuteInMainThreadSync Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~ExecuteInMainThreadSync.html

---

Execute this work in a synchronous main thread.

Syntax

**C#**



public object ExecuteInMainThreadSync( 

   ExecuteInEplanMainThreadDelegate3 pExecuteDelegate,

   object x

)

public:

Object^ ExecuteInMainThreadSync( 

   ExecuteInEplanMainThreadDelegate3^ pExecuteDelegate,

   Object^ x

)


#### Parameters

*pExecuteDelegate*
:   The work to be done.

*x*

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when no MainThreadDispatcher was set. |
