# ProductGroup Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ProductGroup.html

---

Gets/Sets the product group of the part.

Syntax

**C#**



public virtual MDPartsDatabaseItem.Enums.ProductGroup ProductGroup {get; set;}

public:

virtual property MDPartsDatabaseItem.Enums.ProductGroup ProductGroup {

   MDPartsDatabaseItem.Enums.ProductGroup get();

   void set (    MDPartsDatabaseItem.Enums.ProductGroup value);

}


#### Property Value

Product group of the part.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if cannot set given ProductGroup for the current GenericProductGroup of the part. |
