# Document Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~Document.html

---

Determines whether a document is selected. This will only return a document, when the selection is inside the graphical editor.

Syntax

**C#**



public DocumentBase Document {get;}

public:

property DocumentBase^ Document {

   DocumentBase^ get();

}


#### Property Value

the document selected and null if not available.
