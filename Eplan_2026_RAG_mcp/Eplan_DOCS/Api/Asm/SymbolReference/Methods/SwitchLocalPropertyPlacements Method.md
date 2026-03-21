# SwitchLocalPropertyPlacements Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SwitchLocalPropertyPlacements.html

---

Copies or removes all local ProperyPlacemnets and sets flag

Syntax

**C#**



public void SwitchLocalPropertyPlacements( 

   bool nUseLocal

)

public:

void SwitchLocalPropertyPlacements( 

   bool nUseLocal

)


#### Parameters

*nUseLocal*
:   If true copies all properties from symbol/symbol reference . Otherwise removes all local properties.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) | Thrown when user wants to change PropertyPlacement with default configuration. |
