---
title: "Nested structures"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/reftextgen_r_nested_structures.htm"
file: "reftextgen_r_nested_structures"
category: "reftextgen"
---

# Nested structures

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Nested structures Text generator Control structures can be nested as in a programming language. [Example](javascript:void\(0\);)
    
        (*{LOOP:dos}*)
    	(*{IF $Group="Cyclic"}*)
    		//True
    	(*{ELSE}*)
    		//False
    	(*{END_IF}*)
    (*{END_LOOP}*)
