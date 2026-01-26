# Type Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDAddress~Type.html

---

Returns the part type of the part.

Syntax

**C#**



public override MDPartsDatabaseItem.Enums.Type Type {get; set;}

public:

property MDPartsDatabaseItem.Enums.Type Type {

   MDPartsDatabaseItem.Enums.Type get() override;

   void set (    MDPartsDatabaseItem.Enums.Type value) override;

}


#### Property Value

part type of the part (Component, Assembly, Module, Construction, ConnectionPointInfo, Customer, Manufacturer)
