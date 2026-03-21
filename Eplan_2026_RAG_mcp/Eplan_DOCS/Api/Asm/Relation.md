# Relation

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Relation.html

---

Relation class is used as a generic mechanism to navigate in the datamodel from one object to another or to more objects. In the case of the [PlaceHolderText](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlaceHolderText.html) object, user can read it's Relation object, that represents the link to another object and it's property. Value of this property will be displayed in this PlaceholderText in GUI, e.g. at reports page.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      **Eplan.EplApi.DataModel.Relation**

Syntax

**C#**



public struct Relation : System.ValueType

public value class Relation : public System.ValueType

Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Index](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Relation~Index.html) | Relation-Index - which object to get. if index is equal to 0 list of objects will be returned. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [ToInt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Relation~ToInt.html) | Relation-Id - identifies which type of navigation will be done. |


