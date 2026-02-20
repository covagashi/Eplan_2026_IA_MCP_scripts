# CanAccessMainThread Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Internal.EplanMainThreadDispatcher~CanAccessMainThread.html

---

Allows the user to access the main thread both synchronously and asynchronously.

Syntax

**C#**



public static bool CanAccessMainThread()

public:

static bool CanAccessMainThread();


#### Return Value

True then execution is possible.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when no MainThreadDispatcher was set. |
