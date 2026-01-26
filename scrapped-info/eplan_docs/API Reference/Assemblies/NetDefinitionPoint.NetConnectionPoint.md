# NetDefinitionPoint.NetConnectionPoint

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint.html

---

Represents connection points of a net

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)  
      **Eplan.EplApi.DataModel.NetDefinitionPoint.NetConnectionPoint**

Syntax

**C#**



public class NetDefinitionPoint.NetConnectionPoint : PinBase

public ref class NetDefinitionPoint.NetConnectionPoint : public PinBase

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [NetDefinitionPoint.NetConnectionPoint Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint~_ctor.html) |  |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Direction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Direction.html) | Gets the connection point's direction. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [IdForNetBasedConnections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint~IdForNetBasedConnections.html) | Returns Id for net-based connections |
| Public Property | [Index](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Index.html) | Returns an index of this connection point. NOTE: This may be an index amongst a function's conn. points (in case this object represents a 'logical' conn. point) or an index amongst a symbol's conn. points (in case this object is just a graphical conn. point of a symbol). (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Location.html) | Gets the connection point's position relative to the symbol's insertion point. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint~Name.html) | Returns name of a connection point |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Parent.html) | Returns the symbol reference that the logical conn. point represented by this object belongs to. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Dispose().html) | Destructor for deterministic finalization of ViewPlacement object. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Equals.html) | Comparison of two PinBase objects. Comparison is made by comparing each of Pin members instead of internal object id. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.PinBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html)) |
| Public Method | [ToString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint~ToString.html) | Returns a string that represents the current object. |


