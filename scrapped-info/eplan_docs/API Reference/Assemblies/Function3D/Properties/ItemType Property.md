# ItemType Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D~ItemType.html

---

Item type of this Function3D, corresponds to value of the 'Item' list in GUI.

Syntax

**C#**



public ItemType ItemType {get; set;}

public:

property ItemType ItemType {

   ItemType get();

   void set (    ItemType value);

}


#### Property Value

Item type of Function3D or if for [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of this Function3D there exists only one ItemType value ItemType::Unknown will be returned.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `Enums::ItemType` is not valid. |
