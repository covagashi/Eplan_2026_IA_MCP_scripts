# Property(AnyPropertyId,Int32) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Property(AnyPropertyId,Int32).html

---

Method used by operator[] in order to access indexed properties by AnyPropertyId.

Syntax

**C#**



public PropertyValue Property( 

   AnyPropertyId propertyId,

   int index

) {get; set;}

public:

property PropertyValue^ Property {

   PropertyValue^ get(AnyPropertyId^ propertyId, int index);

   void set (AnyPropertyId^ propertyId, int index, PropertyValue^ value);

}


#### Parameters

*propertyId*


*index*
:   Index of the property

#### Property Value

[PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) Object that automatically converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [InvalidIndexException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidIndexException.html) | InvalidIndexException |
| [SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |

Remarks

To check if property with given id can be set on this property list please check it using [Exists(AnyPropertyId)](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Exists(AnyPropertyId).html) method.
