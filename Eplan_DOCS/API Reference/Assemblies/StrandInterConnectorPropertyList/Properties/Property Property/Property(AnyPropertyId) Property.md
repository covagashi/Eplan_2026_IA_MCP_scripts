# Property(AnyPropertyId) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StrandInterConnectorPropertyList~Property(AnyPropertyId).html

---

Method used by operator[] in order to access properties by AnyPropertyId.

Syntax

**C#**



public new PropertyValue Property( 

   AnyPropertyId propertyId

) {get; set;}

public:

new property PropertyValue^ Property {

   PropertyValue^ get(AnyPropertyId^ propertyId);

   void set (AnyPropertyId^ propertyId, PropertyValue^ value);

}


#### Parameters

*propertyId*

#### Property Value

[PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) Object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
