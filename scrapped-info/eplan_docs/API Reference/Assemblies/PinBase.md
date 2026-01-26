# PinBase

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase.html

---

This class represents a symbol's connection point (i.e. graphical conn. point) or is the base class for representation of a function's connection point (i.e. logical conn. point).

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.PinBase**  
      [Eplan.EplApi.DataModel.NetDefinitionPoint.NetConnectionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint+NetConnectionPoint.html)  
      [Eplan.EplApi.DataModel.Pin](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Pin.html)

Syntax

**C#**



public class PinBase

public ref class PinBase

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PinBase Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Direction](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Direction.html) | Gets the connection point's direction. |
| Public Property | [Index](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Index.html) | Returns an index of this connection point. NOTE: This may be an index amongst a function's conn. points (in case this object represents a 'logical' conn. point) or an index amongst a symbol's conn. points (in case this object is just a graphical conn. point of a symbol). |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Location.html) | Gets the connection point's position relative to the symbol's insertion point. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Parent.html) | Returns the symbol reference that the logical conn. point represented by this object belongs to. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Dispose().html) | Destructor for deterministic finalization of PinBase object. |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~Equals.html) | Comparison of two PinBase objects. Comparison is made by comparing each of Pin members instead of internal object id. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~GetHashCode.html) | Serves as the default hash function. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~op_Equality.html) | .NET operator for comparing two PinBase objects. |
| public Operator [Inequality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~op_Inequality.html) | .NET operator for comparing two PinBase objects. |


