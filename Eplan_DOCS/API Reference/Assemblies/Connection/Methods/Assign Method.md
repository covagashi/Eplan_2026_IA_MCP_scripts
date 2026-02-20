# Assign Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~Assign.html

---

Assigns this connection to another, which means that values of this connection's properties are copied to the target connection and the source connection itself is removed from the project.

Syntax

**C#**



public void Assign( 

   Connection targetConn

)

public:

void Assign( 

   Connection^ targetConn

)


#### Parameters

*targetConn*
:   The target connection whose properties are set with values from this connection.

Remarks

\* This method corresponds to the 'Assign' action called from the device navigator's context menu. \* After the assignment, this connection becomes the target connection.
