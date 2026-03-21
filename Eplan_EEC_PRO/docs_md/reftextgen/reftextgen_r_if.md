---
title: "IF"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/reftextgen_r_if.htm"
file: "reftextgen_r_if"
category: "reftextgen"
---

# IF

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  IF Text generator IF checks the truth value of a condition, which is described by a formula. If the truth value is true then the condition is satisfied and the following operation is executed. If the truth value is false then the following operation is skipped. Further conditions can be expressed with ELSE, whose truth value is checked afterwards. ELSE checks the truth value of a further condition after the result of a previous condition is false. ELSE is optional, that means, for example, if in the ELSE case no text is created, then the ELSE branch may be omitted. ENDIF ends the control structure. [Example](javascript:void\(0\);)
    
        (*{IF $Group="Cyclic"}*) true
    (*{ELSE}*) false
    (*{END_IF}*)
    oder:
    (*{IF $Group="Cyclic"}*) true
    (*{END_IF}*)
