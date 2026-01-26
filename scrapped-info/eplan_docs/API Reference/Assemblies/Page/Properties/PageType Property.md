# PageType Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html

---

Gets/sets a page's property describing type of document

Syntax

**C#**



public DocumentTypeManager.DocumentType PageType {get; set;}

public:

property DocumentTypeManager.DocumentType PageType {

   DocumentTypeManager.DocumentType get();

   void set (    DocumentTypeManager.DocumentType value);

}


#### Property Value

DocumentType : enum type with available types of document

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the document type cannot be read form data model. |
