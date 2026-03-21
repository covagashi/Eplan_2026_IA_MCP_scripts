---
title: "key(Object value)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_bidimap_key.htm"
file: "refformulas_r_map_bidimap_key"
category: "refformulas"
---

# key(Object value)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  key(Object value) Methods for BidiMap Returns the key for the value. The result is <<null>> if the key is not included. If a value exists more than once, one of the values is returned, that means BidiMaps should only be used in cases where either the key and the value are unique. key(Object value)  
---  
Argument | Object | value | Value for which the key is sought.  
Return value | key | Key for the value  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=Map{Pair{'A',1}, Pair{'B',2}}.key(1) | A
