# Pin

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html

---

This class represents a function's connection point.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)  
      **Eplan.EplApi.DataModel.Pin**

Syntax

**C#**



public sealed class Pin : PinBase

public ref class Pin sealed : public PinBase


Remarks

\* Function's connection points are sometimes called 'logical' since they have some properties stored in the function's logic, as opposed to 'graphical' connection points of symbols which only carry graphical information (relative location, direction, etc). \* A logical connection point may be mapped to the underlying symbol's connection point and return graphical information (location, direction, etc) through properties of the base class or through the Pin::SymbolConnectionPoint property. \* Logical connection points may also be returned by a FunctionDefinition object. Such conn. points are not associated with any function so their ParentFunction property, as well as some other properties, are NULL.

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AreSameConnectionPointDesignationsAllowed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~AreSameConnectionPointDesignationsAllowed.html) | Determines if similar connection point designations are allowed. |
| Public Property | [Connections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Connections.html) | Returns connections which start or end at this connection point. |
| Public Property | [ConsumerSources](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~ConsumerSources.html) | consumer source |
| Public Property | [Designation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Designation.html) | Returns internal designation of this pin. |
| Public Property | [Direction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Direction.html) | Gets the connection point's direction. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~FunctionDefinition.html) | A FunctionDefinition object that this connection point belongs to. |
| Public Property | [Index](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Index.html) | Returns an index of this connection point. NOTE: This may be an index amongst a function's conn. points (in case this object represents a 'logical' conn. point) or an index amongst a symbol's conn. points (in case this object is just a graphical conn. point of a symbol). (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [IntrinsicSafetyPossible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~IntrinsicSafetyPossible.html) | Determines if intrinsic safety is possible. |
| Public Property | [isCableConnectionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~isCableConnectionPoint.html) | Assigns whether it is possible to connect a cable to the Pin. |
| Public Property | [IsExtern](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~IsExtern.html) | Qualify the Pin is extern or intern. |
| Public Property | [IsSourceOrTarget](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~IsSourceOrTarget.html) | Gets/Sets pin's SourceOrTarget. |
| Public Property | [JumperBarCount](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~JumperBarCount.html) | Assigns the maximum number of JumperBars on the Pin. |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Location.html) | Gets the connection point's position relative to the symbol's insertion point. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [MaxConnectionCount](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~MaxConnectionCount.html) | The maximum number of Connections on the Pin. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Name.html) | Gets the pin's actual designation. This value is equal to FUNC\_CONNECTIONDESIGNATION property of the parent function, at the corresponding index. |
| Public Property | [OppositePin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~OppositePin.html) | Gets/Sets the potential forwarding for connections of the same function or connections of different functions of the same device. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Parent.html) | Returns the symbol reference that the logical conn. point represented by this object belongs to. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [ParentFunction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~ParentFunction.html) | Returns a function that this connection point belongs to. |
| Public Property | [PinPotential](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~PinPotential.html) | Assigns a PotentialType to the Pin. |
| Public Property | [PlcTracking](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~PlcTracking.html) | Assigns a pin designation or index for PLC tracking. |
| Public Property | [Signal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Signal.html) | Assigns a SignalType to the Pin. |
| Public Property | [SymbolConnPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~SymbolConnPoint.html) | Gets/Sets the underlying symbol's connection point assigned to this pin or `null`. |
| Public Property | [TargetCount](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~TargetCount.html) | Returns number of connections from this Pin object. |
| Public Property | [TargetPins](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~TargetPins.html) | Returns Pin objects of other functions connected directly with this conn. point. |
| Public Property | [Type](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Type.html) | Assigns a ConnPointType to the Pin. |
| Public Property | [TypeOfPort](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~TypeOfPort.html) | Assigns a PortType to the Pin. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Dispose().html) | Destructor for deterministic finalization of Pin object. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~Equals.html) | Overridden. Comparison of two PinBase objects. Comparison is made by comparing each of Pin members instead of internal object id. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~GetHashCode.html) | Overridden. Serves as the default hash function. |
| Public Method | [ToString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~ToString.html) | Returns a string that represents the current object. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin~op_Equality.html) | .NET operator for comparing two Pin objects. Comparison is made by comparing each of Pin members instead of internal object id. |


