# ItemType Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDMechanicsFunctionDefinition~ItemType.html

---

Gets/Sets item of the function definition.

Syntax

**C#**



public ItemType ItemType {get; set;}

public:

property ItemType ItemType {

   ItemType get();

   void set (    ItemType value);

}


#### Property Value

Placement3D::Enums::AdditionalType enum value.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if cannot set given Placement3D::Enums::AdditionalType enum value from parameter for the current function definition. |
