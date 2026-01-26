# ProductSubGroup Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ProductSubGroup.html

---

Gets/Sets the product sub group of the part.

Syntax

**C#**



public virtual MDPartsDatabaseItem.Enums.ProductSubGroup ProductSubGroup {get; set;}

public:

virtual property MDPartsDatabaseItem.Enums.ProductSubGroup ProductSubGroup {

   MDPartsDatabaseItem.Enums.ProductSubGroup get();

   void set (    MDPartsDatabaseItem.Enums.ProductSubGroup value);

}


#### Property Value

Product sub group of the part

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown if cannot set given ProductSubGroup for the current ProductGroup of the part. |
