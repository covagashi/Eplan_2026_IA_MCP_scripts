# TargetIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~TargetIndex.html

---

Terminal designation 1-base index.

Syntax

**C#**



public int TargetIndex {get; set;}

public:

property int TargetIndex {

   int get();

   void set (    int value);

}


Remarks

This is a special feature for terminals, because the terminals have only a terminal number and the connection point designations are often empty. In such case routing algorithms can't decide which connection point will be used for a connection. The routing algorithms use the target index (first destination, second destination, ...) of a connection point in 2D, to determine the right terminal position in 3D or topologies.
