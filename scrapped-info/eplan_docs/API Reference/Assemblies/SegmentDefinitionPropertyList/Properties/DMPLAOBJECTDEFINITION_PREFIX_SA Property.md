# DMPLAOBJECTDEFINITION_PREFIX_SA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1070.html

---

Method used by operator[] in order to access indexed properties.

Syntax

**C#**



public PropertyValue Property( 

   Properties.SegmentDefinition id,

   int index

) {get; set;}

public:

property PropertyValue^ Property {

   PropertyValue^ get(Properties.SegmentDefinition id, int index);

   void set (Properties.SegmentDefinition id, int index, PropertyValue^ value);

}


#### Parameters

*id*
:   Identifier of the SegmentDefinition's property

*index*
:   Index of the SegmentDefinition's property

#### Property Value

[Eplan.EplApi.DataModel.PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) object that automaticaly converts into common used types.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown in case of an external error. Please refer to the exception message. |
| [Eplan.EplApi.DataModel.PropertyNotFoundException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyNotFoundException.html) | PropertyNotFoundException |
| [Eplan.EplApi.DataModel.InvalidIndexException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidIndexException.html) | InvalidIndexException |
| [Eplan.EplApi.DataModel.PropertyReadOnlyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyReadOnlyException.html) | PropertyReadOnlyException |
| [Eplan.EplApi.DataModel.SettingValueFailedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SettingValueFailedException.html) | SettingValueFailedException |
