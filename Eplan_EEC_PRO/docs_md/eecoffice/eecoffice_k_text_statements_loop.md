---
title: "LOOP"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_text_statements_loop.htm"
file: "eecoffice_k_text_statements_loop"
category: "eecoffice"
---

# LOOP

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## LOOP

The LOOP constructor is used to iterate through a collection of fragments and to insert the part of the document contained within the LOOP once for each element, as well as to run any existing commands belonging to the loop.

Like the IF control structure, LOOP consists of two parts that bracket a section of the document. A LOOP control structure begins with (*{LOOP:<Collection>}*), where <Collection> is a formula that must return a collection of fragments. The end of the LOOP control structure is signaled by (*{END_LOOP}*) (see also [Collections (Collections Of Objects)](refformulas_r_collections.htm)).

Everything contained within the LOOP control structure is inserted into the target document for each element in the collection. This means that the text between the LOOP control structures are inserted multiple times, including all line breaks, formats, etc.

The boundaries are as follows:

     * the first character after (*{LOOP:<Formula>}*)
     * the last character before (*{END_LOOP}*)

Within the LOOP control structures, line breaks, page breaks, etc. count as characters. In the process, all paragraphs, formatting, line breaks, etc. are preserved exactly and are replicated for each element on the list.

This procedure may be compared to the following manual operation:

The area contained within the LOOP control structure is selected and copied to the clipboard. The cursor is then positioned right at the beginning of the (*{END_LOOP}*) structure and the contents of the clipboard are pasted there. This is performed once for each element in the collection. Next, the (*{LOOP: <Collection>}*) and (*{END_LOOP}*) structures are deleted from the text, without changes being made to the paragraph boundaries, line breaks, or other structural formatting.

In the case of an empty collection, the enclosed area does not remain within the document; as with an IF structure that evaluates to false, it is deleted from the document without leaving a trace behind.

In addition to the ability to repeat identical text multiple times, fragments can also be inserted into the target document. To accomplish this, a (*{Content}*) control structure must be built within the LOOP control structure. For this control structure, the content of the fragment is inserted for each element in the collection. No additional line breaks, paragraphs or other formatting is inserted in the process.

### [Syntax example](javascript:void\(0\);)
    
        (*{LOOP:dos('Word.WordComponent')}*)(*{Content}*)(*{END_LOOP}*)

For fragments consisting of one paragraph, the formatting of the first character of the (*{Content}*) control structure is adopted. This includes not only simple formatting such as bold, _italics_ or _underline_ , but style sheets as well.

For fragments consisting of multiple paragraphs, the formatting of the first character of the (*{Content}*) control structure is used for the first paragraph. All subsequent paragraphs use the style sheet from the fragment. If the target document lacks the corresponding style sheet, it is inserted there as a copy.

In addition to whole documents, a formula can be evaluated via (*{<Formula>}*) in the context of each active object within the LOOP, and the result can be inserted into the main document as a text form. In this case, the formatting of the first character of the (*{<Formula>}*) control structure is used for all of the content.
