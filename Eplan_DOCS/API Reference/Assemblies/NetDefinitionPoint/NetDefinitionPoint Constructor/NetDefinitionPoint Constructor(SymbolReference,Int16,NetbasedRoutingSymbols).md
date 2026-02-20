# NetDefinitionPoint Constructor(SymbolReference,Int16,NetbasedRoutingSymbols)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NetDefinitionPoint~_ctor(SymbolReference,Int16,NetbasedRoutingSymbols).html

---

Creates a NetDefinitionPoint object.

Syntax

**C#**



public NetDefinitionPoint( 

   SymbolReference pSymbolRef,

   short Index,

   NetDefinitionPoint.NetbasedRoutingSymbols routingSymbols

)

public:

NetDefinitionPoint( 

   SymbolReference^ pSymbolRef,

   short Index,

   NetDefinitionPoint.NetbasedRoutingSymbols routingSymbols

)


#### Parameters

*pSymbolRef*
:   The NetDefinitionPoint object will be created on the connection attached to this SymbolReference.

*Index*
:   Index of the connection point (PinBase.Index) of the SymbolReference, where the connection is attached.

*routingSymbols*
:   Set 'Yes' if routing symbol for netbased wiring should be used. The value can either be 'Yes', 'No', or it can be taken from the settings

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a NetDefinitionPoint cannot be created. |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
