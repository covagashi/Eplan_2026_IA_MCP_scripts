# SymbolicAddress Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegment+PLCAddress~SymbolicAddress.html

---

A single component of the symbolic address can be entered at structure segments and planning objects . These single components are linked at the PLC inputs and outputs of the planning objects starting with the top node and displayed in the Symbolic address (pre-planning) property. This procedure allows unique symbolic addresses to be created for the PLC inputs and outputs. The automatic symbolic address.

Syntax

**C#**



public string SymbolicAddress {get; set;}

public:

property String^ SymbolicAddress {

   String^ get();

   void set (    String^ value);

}


Remarks

If the user did not set this property or the SymbolicAddressPart is not empty then the returned value is generated automatically. The value is generated from symbolic addresses stored at structure segments and planning objects. These single components are linked at the PLC inputs and outputs of the planning objects starting with the top node and displayed in the Symbolic address (pre-planning) property. This procedure allows unique symbolic addresses to be created for the PLC inputs and outputs.
