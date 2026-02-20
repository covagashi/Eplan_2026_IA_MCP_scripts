# Property(MDAnyPropertyId) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~Property(MDAnyPropertyId).html

---

Method used by operator[] in order to access properties by MDAnyPropertyId.

Syntax

**C#**



public new MDPropertyValue Property( 

   MDAnyPropertyId id

) {get; set;}

public:

new property MDPropertyValue^ Property {

   MDPropertyValue^ get(MDAnyPropertyId^ id);

   void set (MDAnyPropertyId^ id, MDPropertyValue^ value);

}


#### Parameters

*id*
:   Identifier of the property

#### Property Value

[MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) Object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [MDPropertyNotFoundException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyNotFoundException.html) | MDPropertyNotFoundException |
