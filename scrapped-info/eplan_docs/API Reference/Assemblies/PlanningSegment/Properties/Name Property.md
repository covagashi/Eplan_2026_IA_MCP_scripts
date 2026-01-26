# Name Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment~Name.html

---

Returns the name of planning segment.

Syntax

**C#**



public string Name {get; set;}

public:

property String^ Name {

   String^ get();

   void set (    String^ value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown while setting if new value is `null`. |
| [System.InvalidOperationException](#) | Thrown while setting new value on PCTLoop. |
