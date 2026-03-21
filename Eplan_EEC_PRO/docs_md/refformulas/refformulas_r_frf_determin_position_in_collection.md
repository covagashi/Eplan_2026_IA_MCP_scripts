---
title: "Determining the position of the current element in a Collection"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_frf_determin_position_in_collection.htm"
file: "refformulas_r_frf_determin_position_in_collection"
category: "refformulas"
---

# Determining the position of the current element in a Collection

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Determining the position of the current element in a Collection It is often required to determine the position of a mechatronic object within the children of a mechatronic component
    
        mc.mos.indexOf(this)

This applies if the first object has the index "0". If the count should start at "1" the formula is to be extended as follows:
    
        mc.mos.indexOf(this)+1
