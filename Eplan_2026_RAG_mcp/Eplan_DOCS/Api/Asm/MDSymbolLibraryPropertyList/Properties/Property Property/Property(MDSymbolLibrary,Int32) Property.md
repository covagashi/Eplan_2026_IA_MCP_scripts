# Property(MDSymbolLibrary,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~Property(MDSymbolLibrary,Int32).html

---

Method used by operator[] in order to access indexed properties.

Syntax

**C#**



public MDPropertyValue Property( 

   Properties.MDSymbolLibrary id,

   int index

) {get; set;}

public:

property MDPropertyValue^ Property {

   MDPropertyValue^ get(Properties.MDSymbolLibrary id, int index);

   void set (Properties.MDSymbolLibrary id, int index, MDPropertyValue^ value);

}


#### Parameters

*id*
:   Identifier of the MDSymbolLibrary's property

*index*
:   Index of the MDSymbolLibrary's property

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
