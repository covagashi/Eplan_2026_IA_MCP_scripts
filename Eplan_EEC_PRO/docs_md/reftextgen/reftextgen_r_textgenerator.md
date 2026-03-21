---
title: "Text generator"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/reftextgen_r_textgenerator.htm"
file: "reftextgen_r_textgenerator"
category: "reftextgen"
---

# Text generator

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Text generator The text generator is used to create documents of the text and PLC disciplines. The text generator is controlled by the following elements of the text generator language.
     * Control structures are used to conditional create text (see [IF](reftextgen_r_if.htm)) and iterating over several objects (see [LOOP](reftextgen_r_loop.htm)). By means of control structures, for example, code fragments of a PLC program can be deleted or added.
     * Methods are used in particular by generators of the PLC discipline. They serve, for example, the creation of temporary variables, or the generation of block calls.
     * Formulas can be used to create variable text.
     * Replace parameters are used to exchange text according to the search-and-replace principle.
All elements of the text generator language (with the exception of the [Replace parameters](reftextgen_r_replace_parameter.htm) and [Comments](reftextgen_r_comments.htm)) begin with (*{ and end with }*), e. g. (*{CALL}*). The upper and lower case is important to note in the text generator language. The elements of the text generator language are removed from the template and replaced by the result text whilst generating. No line breaks, tabulators or others will be created, that means the formatting of the template remains in the generated text. More: [Control structures](reftextgen_r_control_structures.htm) [Methods for PLC disciplines](reftextgen_r_plc_discipline_methods.htm) [Formulas](reftextgen_r_formulas.htm) [Replace parameters](reftextgen_r_replace_parameter.htm)
