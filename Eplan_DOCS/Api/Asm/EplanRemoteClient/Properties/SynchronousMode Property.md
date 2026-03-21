# SynchronousMode Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.RemoteClientu~Eplan.EplApi.RemoteClient.EplanRemoteClient~SynchronousMode.html

---

Sets and gets the Synchronous mode.

Syntax

**C#**



public bool SynchronousMode {get; set;}

public:

property bool SynchronousMode {

   bool get();

   void set (    bool value);

}


Remarks

This property is set per default to false. This means, per default all calls, except Connect, are executed asynchronously. You can change this behavior by setting this property to true in order to make synchronous calls. When doing asynchronous calls there is no return values. The Server sends a response (EplanResponse) when the call is executed completely.
