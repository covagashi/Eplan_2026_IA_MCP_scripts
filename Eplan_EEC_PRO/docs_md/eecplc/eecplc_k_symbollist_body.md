---
title: "Body objects"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_symbollist_body.htm"
file: "eecplc_k_symbollist_body"
category: "eecplc"
---

# Body objects

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Body objects

In general, the body contains both a header and a footer line, if the target system requires them. In STEP 7, for example, there is no header and footer. However, the body certainly does include a line containing the formula for assembling the components of the hierarchically lower level. As in the text discipline the general formula is:
    
        (*{LOOP:dos}*)(*{Content}*)(*{END_LOOP}*)

When platform-specific objects are used, the syntax can be changed as follows:
    
        (*{LOOP:CalledPOUs}*)(*{Call}*)(*{END_LOOP}*)

In general, the subordinate elements are the lines. The formula initially assembles all of the sub-elements in the discipline structure into a temporary collection using the dos or CalledPOUs method. If the sub-elements are the lines, this results in a collection of lines. Next, the formula iterates through every element in the collection and inserts them individually into the body in place of the keyword content or call. It is not necessary to include an additional line feed in the lines; this is added automatically at the end of every iteration step.

### Note

The formulas may not contain any blanks. Blanks in the formulas have the effect that an additional double quote is inserted at the beginning of a cillected line, for example ""Symbol","Address","Type".
