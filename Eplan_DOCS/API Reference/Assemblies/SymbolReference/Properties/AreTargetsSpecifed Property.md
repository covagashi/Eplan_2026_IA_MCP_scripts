# AreTargetsSpecifed Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~AreTargetsSpecifed.html

---

The value determines if target is taken from net-based routing or not.

Syntax

**C#**



public bool AreTargetsSpecifed {get; set;}

public:

property bool AreTargetsSpecifed {

   bool get();

   void set (    bool value);

}


Remarks

If for T-node target is determined by net-base routing, this property must be set to false. See also Eplan Help->Working with Connections->Net-Based Connections
