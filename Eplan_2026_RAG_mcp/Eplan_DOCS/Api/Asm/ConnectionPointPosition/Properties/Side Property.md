# Side Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointPosition~Side.html

---

Flag describing if this connection point is internal or external end of connection.

Syntax

**C#**



public ConnectionPointSide Side {get; set;}

public:

property ConnectionPointSide Side {

   ConnectionPointSide get();

   void set (    ConnectionPointSide value);

}


Remarks

This is a special feature for terminals, because the terminals have only a terminal number and the connection point designations are often empty. In such case routing algorithms can't decide which connection point will be used for a connection. The routing algorithms use the external/internal flag of a connection point in 2D, to determine the right terminal position in 3D or topologies.

For non-terminals this property will not be stored after executing `StoreToObject`.
