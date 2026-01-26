# CPU Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment+PLCAddress~CPU.html

---

The name of the CPU for the PLC box to which the PLC connection point belongs.

Syntax

**C#**



public string CPU {get; set;}

public:

property String^ CPU {

   String^ get();

   void set (    String^ value);

}


Remarks

A CPU is identified uniquely through the specification of the configuration project, station ID, and CPU name.
