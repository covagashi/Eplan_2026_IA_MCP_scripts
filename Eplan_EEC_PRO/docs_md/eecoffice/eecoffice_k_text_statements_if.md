---
title: "IF"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_text_statements_if.htm"
file: "eecoffice_k_text_statements_if"
category: "eecoffice"
---

# IF

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

IF

## IF

The IF control structure is used to show or hide part of a document depending on a formula (see also [Formula language](refformulas_r_formula_language.htm)). To accomplish this, an (*{IF formula}*) is used to specify the beginning of the content in question and (*{END_IF}*) is used to mark the end of the block. The formula must return either true or false as a result. During generation, the formula is evaluated in the context of the fragment document or template document to which the Word file is attached as a resource. Within a formula, this refers to the fragment object or template document object.

If the formula returns a true result, the content is embedded in the document between IF and END_IF. If it returns false, the parts are deleted from the document.

In addition, an (*{ELSE}*) can be added to an IF structure. This makes it possible to select exactly one of two pieces of content on the basis of a formula. If the formula for the IF block evaluates to true, then all of the content up to (*{ELSE}*) is left in the document, while the content from (*{ELSE}*) to (*{END_IF}*) is deleted. If the condition evaluates to false, then the generator deletes everything from (*{IF Formula}*) to (*{ELSE}*) from the document, while leaving everything from (*{ELSE}*) to (*{END_IF}*) in the document.
