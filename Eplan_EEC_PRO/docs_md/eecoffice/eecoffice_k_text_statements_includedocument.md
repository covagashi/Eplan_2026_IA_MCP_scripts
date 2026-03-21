---
title: "IncludeDocument"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_text_statements_includedocument.htm"
file: "eecoffice_k_text_statements_includedocument"
category: "eecoffice"
---

# IncludeDocument

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## IncludeDocument

If static content is to be inserted at a specific point in the target document, this can be accomplished using the following command structure: (*{IncludeDocument:<Formula>}*). The <Formula> returns the absolute path to a DOCX file (path specifications generally contain special characters, e.g. backslash \, that have to be escaped accordingly, e.g. \\\. See [Escape sequences](refformulas_r_escape_sequences.htm)). The content of the specified DOCX file is copied into the target document with the formatting preserved.

Example for the referencing of an absolute file name:
    
        (*{IncludeDocument:= 'C:\\temp\\MyFile1.docx'}*)

Example for the referencing of a parameter which as a value contains the absolute path to the DOCX file:
    
        (*{IncludeDocument:= parameter('myFile1').value}*)
