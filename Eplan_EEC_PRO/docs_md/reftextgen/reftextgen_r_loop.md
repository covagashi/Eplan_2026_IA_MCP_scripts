---
title: "LOOP"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/reftextgen_r_loop.htm"
file: "reftextgen_r_loop"
category: "reftextgen"
---

# LOOP

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  LOOP Text generator LOOP iterates over an object list. The list of objects is created by a formula, that returns a list (e.g. dos). Method calls within LOOP will be sent to the object from the object list. The control structure ends with END_LOOP. [Example](javascript:void\(0\);)
    
        (*{LOOP:dos}*)
    (*{name}*)
    (*{END_LOOP}*)

Within LOOP can also be used an index variable. Method calls within LOOP with index variable will be sent to the object that is connected to the text. For Method calls for objects from a object list, the index variable is used. [Example](javascript:void\(0\);)
    
        (*{LOOP:x|List{0..10}*)
    Name des Objekts auÃerhalb von LOOP=(*{name}*)
    Name des Objekts an Position (*{x+1}*)=(*{dc.dos.at(x).name}*)
    (*{END_LOOP}*)
