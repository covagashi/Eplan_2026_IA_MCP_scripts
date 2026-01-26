# InsertedItems Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction~InsertedItems.html

---

Returns placements inserted by interaction.

Syntax

**C#**



public virtual StorableObject[] InsertedItems {get; set;}

public:

virtual property array<StorableObject^>^ InsertedItems {

   array<StorableObject^>^ get();

   void set (    array<StorableObject^>^ value);

}


Remarks

For overriden interactions this property should be set by interaction itself. For other - custom interactions, this property is availabe to be set manually.
