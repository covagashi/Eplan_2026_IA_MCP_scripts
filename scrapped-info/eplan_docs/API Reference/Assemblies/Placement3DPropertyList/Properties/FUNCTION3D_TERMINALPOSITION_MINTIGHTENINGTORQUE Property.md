# FUNCTION3D_TERMINALPOSITION_MINTIGHTENINGTORQUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic682.html

---

Min. tightening torque # 36095.

Syntax

**C#**



public PropertyValue FUNCTION3D_TERMINALPOSITION_MINTIGHTENINGTORQUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNCTION3D_TERMINALPOSITION_MINTIGHTENINGTORQUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Minimal value of the tightening torque. It is specified in Newton meters. It describes the force with which, for example, a screw is tightened, meaning the force that acts from the drive on the socket.
