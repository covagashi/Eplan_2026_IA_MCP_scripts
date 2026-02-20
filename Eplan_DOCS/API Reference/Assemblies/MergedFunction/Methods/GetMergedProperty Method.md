# GetMergedProperty Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~GetMergedProperty.html

---

Returns value of merged property having given property id.

Syntax

**C#**



public PropertyValue GetMergedProperty( 

   AnyPropertyId propId

)

public:

PropertyValue^ GetMergedProperty( 

   AnyPropertyId^ propId

)


#### Parameters

*propId*
:   [AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) - id of property to read

#### Return Value

[PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) value of the property.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |
