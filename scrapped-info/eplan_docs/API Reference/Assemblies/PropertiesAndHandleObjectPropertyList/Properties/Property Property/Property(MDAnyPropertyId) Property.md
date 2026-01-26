# Property(MDAnyPropertyId) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.PropertiesAndHandleObjectPropertyList~Property(MDAnyPropertyId).html

---

Method used by operator[] in order to access properties using MDAnyPropertyId as index.

Syntax

**C#**



public MDPropertyValue Property( 

   MDAnyPropertyId propertyId

) {get; set;}

public:

property MDPropertyValue^ Property {

   MDPropertyValue^ get(MDAnyPropertyId^ propertyId);

   void set (MDAnyPropertyId^ propertyId, MDPropertyValue^ value);

}


#### Parameters

*propertyId*

#### Property Value

[MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) Object that can be converted automatically into a common type.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [MDPropertyNotFoundException](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyNotFoundException.html) | MDPropertyNotFoundException |
