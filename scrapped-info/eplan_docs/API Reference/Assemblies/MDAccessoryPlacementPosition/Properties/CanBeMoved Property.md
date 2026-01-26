# CanBeMoved Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAccessoryPlacementPosition~CanBeMoved.html

---

Activate this option if the part placed via this installation variant can be moved in the enclosure; deactivate the check box if the part is to be a fixed part of the enclosure.

Syntax

**C#**



public bool CanBeMoved {get; set;}

public:

property bool CanBeMoved {

   bool get();

   void set (    bool value);

}


Remarks

Value is taken and stored in property called EW3\_PROPERTY\_ARTICLEACCESSORYPLACEMENTPOSITION\_MOVABLE.
