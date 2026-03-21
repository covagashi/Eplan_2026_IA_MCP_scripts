---
title: "add(Object key, Object value)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_add_1.htm"
file: "refformulas_r_map_add_1"
category: "refformulas"
---

# add(Object key, Object value)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  add(Object key, Object value) Methods For Map Adds a pair consisting of key (key) and value (value) to the map. An already existing pair with the same key is overwritten. This method is a simple form of add(Pair{key, value}). add(Object key, Object value)  
---  
Arguments | Object | key | Key for the pair to be added.  
Object | value | Value for the pair to be added.  
Return value | Map |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{}.add('Help','help') | [HelpÂ»help]
