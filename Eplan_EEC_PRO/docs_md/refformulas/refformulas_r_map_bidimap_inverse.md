---
title: "inverse()"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_map_bidimap_inverse.htm"
file: "refformulas_r_map_bidimap_inverse"
category: "refformulas"
---

# inverse()

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  inverse() Methods for BidiMap Returns the inverted map. In the inverted map the values of the original map are the keys and the keys of the original map are the values. Duplicate values are removed. The obtained value is random, that means BidiMaps should only be used in cases where either the key and the value are unique. inverse()  
---  
Argument |  |  |   
Return value | BidiMap | BidiMap with exchanged key-value pairs  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=BidiMap{Pair{'A',1}, Pair{'B',2}}.inverse | [1Â»A,2Â»B]
