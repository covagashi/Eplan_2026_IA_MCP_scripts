# Property(MDSymbolVariant,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolVariantPropertyList~Property(MDSymbolVariant,Int32).html

---

Method used by operator[] in order to access indexed properties.

Syntax

**C#**



public MDPropertyValue Property( 

   Properties.MDSymbolVariant id,

   int index

) {get; set;}

public:

property MDPropertyValue^ Property {

   MDPropertyValue^ get(Properties.MDSymbolVariant id, int index);

   void set (Properties.MDSymbolVariant id, int index, MDPropertyValue^ value);

}


#### Parameters

*id*
:   Identifier of the MDSymbolVariant's property

*index*
:   Index of the MDSymbolVariant's property

#### Property Value

[MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [MDPropertyNotFoundException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyNotFoundException.html) | MDPropertyNotFoundException |
| [MDInvalidIndexException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidIndexException.html) | MDInvalidIndexException |
| [MDPropertyReadOnlyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyReadOnlyException.html) | MDPropertyReadOnlyException |
| [MDSettingValueFailedException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSettingValueFailedException.html) | MDSettingValueFailedException |
