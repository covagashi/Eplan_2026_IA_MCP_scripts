# GetFctDocTypesToMerge Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentTypeManager~GetFctDocTypesToMerge.html

---

Returns those page document types, for which a function placed on this page should be considered while merging. I.e. if the function is placed on graphical page, it makes no sense / is incorrect to collect such function.

Syntax

**C#**



public static DocumentTypeManager.DocumentType[] GetFctDocTypesToMerge()

public:

static array<DocumentTypeManager.DocumentType>^ GetFctDocTypesToMerge();

