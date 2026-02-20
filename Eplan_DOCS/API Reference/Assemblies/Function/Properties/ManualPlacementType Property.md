# ManualPlacementType Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~ManualPlacementType.html

---

Gets custom placement type. Placement type express how function will be shown on scheme.

Syntax

**C#**



public DocumentTypeManager.DocumentType ManualPlacementType {get; set;}

public:

property DocumentTypeManager.DocumentType ManualPlacementType {

   DocumentTypeManager.DocumentType get();

   void set (    DocumentTypeManager.DocumentType value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Throws InvalidArgumentType when DocumentType doesn't match to this function. Check [DocumentTypeManager.IsGraphicalFunctionPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager~IsGraphicalFunctionPlacement.html) |
