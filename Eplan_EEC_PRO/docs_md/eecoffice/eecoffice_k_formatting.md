---
title: "Formatting"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_formatting.htm"
file: "eecoffice_k_formatting"
category: "eecoffice"
---

# Formatting

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Formatting

The most important thing for all formattings is that the format names and their format settings are identical in all DOCX files used! As a rule WORD documents are based on the document template Normal.dot and obtain the format templates from this file. All formatting changes should therefore always be created with the underlying document template.

The underlying document template can be changed under Developer tools > Word-Add-Ins, Templates tab. Format changes are automatically transferred into the document template by means of the option Update document format templates automatically. Additional document templates can be added under Global document templates and add-ins. Their formats are then additionally made available in all documents. To transfer the formats already created from any DOCX file into the document template, click [Organize...]. Individual formats can be exchanged in the following dialog between two WORD files.

If the fragment whose content is collected via a loop control structure consists of only a single paragraph, then the content adopts the paragraph format in which the content portion of the control structure is formatted; only character formatting is carried over. This means that the paragraph formatting of the collected fragment document is ignored, but not the character formatting.

### [Example](javascript:void\(0\);)

The control structure of the main or fragment document collecting the content:

(*{LOOP:dos}*)Text before the paragraph to be inserted

(*{Content}*)

Text after the paragraph to be inserted (*{END_LOOP}*)

The paragraph to be collected:

Item _Type_ Designation

Result:

Text before the paragraph to be inserted

Item _Type_ Designation

Text after the paragraph to be inserted

If the fragment whose content is collected via a LOOP control structure consists of more than one paragraph, then the content of the first paragraph adopts the paragraph format in which the content portion of the structure is formatted, while all other paragraphs retain their own paragraph formatting. This means that only the paragraph formatting of the first paragraph of the collected fragment document is ignored.

### [Example](javascript:void\(0\);)

The control structure of the main or fragment document collecting the content:

(*{LOOP:dos}*)Text before the paragraph to be inserted

(*{Content}*)

Text after the paragraph to be inserted (*{END_LOOP}*)

The paragraphs to be collected:

List of sensors/actuators

Item Type Designation

Result:

Text before the paragraph to be inserted

List of sensors/actuators

Item Type Designation

Text after the paragraph to be inserted

If one of the subsequent paragraphs being collected has a format that is not available in the collecting main or fragment document, this formatting is imported into the collecting document.
