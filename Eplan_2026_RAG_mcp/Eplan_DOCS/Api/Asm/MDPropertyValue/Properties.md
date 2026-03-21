# Properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue_properties.html

---

For a list of all members of this type, see [MDPropertyValue members](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue_members.html).

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Definition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Definition.html) | Returns an object that provides information about the property and its definition.  The information includes: name of the property, it's data type, whether it is indexed or not, whether it is read-only, upper/lower bounds of values for numerical properties. |
| Public Property | [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Id.html) | Returns P8-Property descriptor (id and index) of the object.  Offline MDPropertyValue objects don't have descriptors because they point to value directly. An offline MDPropertyValue is created by operators that take base types values. |
| Public Property | [Indexes](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Indexes.html) | Returns array of indexes for which property value is not empty. It can be used with MDPropertyValue::operator []; |
| Public Property | [IsEmpty](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~IsEmpty.html) | Checks if property value is empty. If it's not it can be read.  IMPORTANT: If property is indexed you have to specify index. |
| Public Property | [Item](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Item.html) | Returns [MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object at specified index. |
| Public Property | [LastUsedIndex](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~LastUsedIndex.html) | Returns number of highest used index. Index value starts from 1. If it is a not indexed-property or if their index is not used, LastUsedIndex is 0.  An object of MDPropertyValue has to point to online property. |
| Public Property | [Parent](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Parent.html) | Property list to which this property value is connected. |


