# Terminal.Bridge

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge.html

---

This class represents a collection of all bridge connections attached to a given terminal or, if the terminal is part of a multi-level terminal, all bridge connections attached to one level of the multi-level terminal. When getting bridges through TerminalStrip::Bridges property, this class represents a whole bridge which means that it contains all segments of a given type which are connected together (and not just segments connected directly to one terminal)

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.EObjects.Terminal.Bridge**

Syntax

**C#**



public class Terminal.Bridge

public ref class Terminal.Bridge


Remarks

Each bridge connection (a segment) is represented by an item in the array returned by the [BridgeSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~BridgeSegments.html) property. (Note: a segment is two terminals connected by a single bridge connection.)

Example

**C#**

```
Terminal term1; // A single-level terminal with some bridge connections existing and connected to it

Terminal.Bridge[] arrBridges = term1.Bridges; // For the single-level terminal, if the terminal has any bridge attached,

											  // the array contains 1 element.

Terminal.Bridge.BridgeInfo[] arrBridgeSegments = arrBridges[0].BridgeSegments;  // The arrBridgeSegments array contains as all bridge segments

																				// of the terminal's first bridge.

																				// All bridge connections are included: 

																				// internal, external, saddleslot 3, saddleslot 4 and saddleslot 5

Terminal other = arrBridgeSegments[0].BridgedTerminal;

Connection brCn = arrBridgeSegments[0].Conn;

if (other != null && brCn != null)

{

	// The _term1_ terminal is connected with the _other_ terminal through the _brCn_ connection.

}

Terminal term1of3; // A part of a 3-level terminal.

arrBridges = term1of3.Bridges; // If there's a bridge on each level, the array contains 3 elements.

arrBridgeSegments = arrBridges[0].BridgeSegments; // All bridge connections (i.e. segments) of the first level

arrBridgeSegments = arrBridges[1].BridgeSegments; // All bridge connections of the second level

arrBridgeSegments = arrBridges[2].BridgeSegments; // All bridge connections of the third level

Terminal level3 = arrBridges[2].Term;

other = arrBridges[2].BridgeSegments[0].BridgedTerminal;

brCn = arrBridges[2].BridgeSegments[0].Conn;

if (other != null && brCn != null)

{

	// The _level3_ terminal - the third level of the multi-level terminal - is connected with the _other_ terminal

	// through the _brCn_ connection.

}
```

Public Fields

|  | Name | Description |
| --- | --- | --- |
| Public Field | [BridgeSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~BridgeSegments.html) | An array of all bridge connections (i.e. segments) that the bridge consists of. |
| Public Field | [Term](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Term.html) | One of the terminal connected by the bridge. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [IsVertical](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~IsVertical.html) | Returns information whether the bridge is 'vertical', i.e. whether it connects only different levels of the same multi-level terminal. Note: this property is valid only if the bridge object has been obtained through the TerminalStrip.Bridges\_Split property of a terminal strip object. Otherwise, this property returns FALSE. |
| Public Property | [Kind](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Kind.html) | A [Terminal.Bridge.Kinds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge+Kinds.html) of the bridge (i.e. internal, external, small, saddleslot 3, saddleslot 4 or saddleslot 5). |
| Public Property | [Terminals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Terminals.html) | An array of all terminals that the bridge connects. |
| Public Property | [Type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal+Bridge~Type.html) | A type of the bridge. Corresponds to the function definition tag of the bridge's connections. |


