# PinBase Constructor(Int32,PointD,Directions)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PinBase~_ctor(Int32,PointD,Directions).html

---

Creates a PinBase object representing a graphical connection point of a symbol.

Syntax

**C#**



public PinBase( 

   int pinIdx,

   PointD ptLocation,

   PinBase.Directions dir

)

public:

PinBase( 

   int pinIdx,

   PointD ptLocation,

   PinBase.Directions dir

)


#### Parameters

*pinIdx*
:   Index of this connection point among the symbol's connection points.

*ptLocation*
:   Position of the conn. point relative to the symbol's insertion point.

*dir*
:   Direction of the connection point.

Remarks

The Parent property is not initialized by this constructor.
