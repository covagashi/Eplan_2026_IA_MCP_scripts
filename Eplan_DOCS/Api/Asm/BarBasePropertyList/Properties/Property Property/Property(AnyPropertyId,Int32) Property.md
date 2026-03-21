# Property(AnyPropertyId,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BarBasePropertyList~Property(AnyPropertyId,Int32).html

---

Method used by operator[] in order to access indexed properties by AnyPropertyId.

Syntax

**C#**



public new PropertyValue Property( 

   AnyPropertyId propertyId,

   int index

) {get; set;}

public:

new property PropertyValue^ Property {

   PropertyValue^ get(AnyPropertyId^ propertyId, int index);

   void set (AnyPropertyId^ propertyId, int index, PropertyValue^ value);

}


#### Parameters

*propertyId*


*index*
:   Index of the property

#### Property Value

[Eplan.EplApi.DataModel.PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) Object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [Eplan.EplApi.DataModel.PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [Eplan.EplApi.DataModel.InvalidIndexException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidIndexException.html) | InvalidIndexException |
| [Eplan.EplApi.DataModel.SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |
