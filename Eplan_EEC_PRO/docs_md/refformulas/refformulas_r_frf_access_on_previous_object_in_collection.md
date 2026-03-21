---
title: "Accessing the previous object of a collection"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_frf_access_on_previous_object_in_collection.htm"
file: "refformulas_r_frf_access_on_previous_object_in_collection"
category: "refformulas"
---

# Accessing the previous object of a collection

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Accessing the previous object of a collection This formula is based on the formula for [Determining the position of the current element in a Collection](refformulas_r_frf_determin_position_in_collection.htm). As result, the name of the previous object should be returned. Importantly, however, is to examine the case that the object itself is the first of the collection. This example returns the name of the first object:  
      
        if (mc.mos.indexOf(this)>0) then mc.mos.pre(this).name else name endif
