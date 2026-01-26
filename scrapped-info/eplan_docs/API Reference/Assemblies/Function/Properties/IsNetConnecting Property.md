# IsNetConnecting Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~IsNetConnecting.html

---

Returns, if the function is netconnecting.

Syntax

**C#**



public bool IsNetConnecting {get; set;}

public:

property bool IsNetConnecting {

   bool get();

   void set (    bool value);

}


#### Property Value

true : Function is netconnecting

false : Function is not netconnecting

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be retrieved from data model. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the flag cannot be changed. |
| [System.ArgumentNullException](#) | Thrown when trying to set a function net connecting that separates potentials. |
