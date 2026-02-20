# Property(MDAnyPropertyId,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1733.html

---

Method used by operator[] in order to access indexed properties by MDAnyPropertyId.

Syntax

**C#**



public MDPropertyValue Property( 

   MDAnyPropertyId propertyId,

   int index

) {get; set;}

public:

property MDPropertyValue^ Property {

   MDPropertyValue^ get(MDAnyPropertyId^ propertyId, int index);

   void set (MDAnyPropertyId^ propertyId, int index, MDPropertyValue^ value);

}


#### Parameters

*propertyId*


*index*
:   Index of the property

#### Property Value

[MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) Object that can be converted automatically into a common type.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [MDPropertyNotFoundException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyNotFoundException.html) | MDPropertyNotFoundException |
| [MDInvalidIndexException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDInvalidIndexException.html) | MDInvalidIndexException |
| [MDSettingValueFailedException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSettingValueFailedException.html) | MDSettingValueFailedException |
