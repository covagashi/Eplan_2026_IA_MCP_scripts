# Property(MDPartsDatabaseItem) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~Property(MDPartsDatabaseItem).html

---

Method used by operator[] in order to access properties.

Syntax

**C#**



public MDPropertyValue Property( 

   Properties.MDPartsDatabaseItem id

) {get; set;}

public:

property MDPropertyValue^ Property {

   MDPropertyValue^ get(Properties.MDPartsDatabaseItem id);

   void set (Properties.MDPartsDatabaseItem id, MDPropertyValue^ value);

}


#### Parameters

*id*
:   Identifier of the MDPartsDatabaseItem's property

#### Property Value

[MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [MDPropertyNotFoundException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyNotFoundException.html) | MDPropertyNotFoundException |
| [MDPropertyReadOnlyException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyReadOnlyException.html) | MDPropertyReadOnlyException |
| [MDSettingValueFailedException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSettingValueFailedException.html) | MDSettingValueFailedException |
