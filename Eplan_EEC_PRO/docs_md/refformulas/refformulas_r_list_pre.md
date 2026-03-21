---
title: "pre(Object obj)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_list_pre.htm"
file: "refformulas_r_list_pre"
category: "refformulas"
---

# pre(Object obj)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  pre(Object obj) Methods for list Returns the previous object to obj. pre(Object obj)  
---  
Argument | Object | obj | Object for which the predecessor is sought.  
Return value | Object |  Previous object to obj. If obj is the first object of the list, <null> is returned. If obj is not included in the list, <null> is also returned.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{1,2,3,4}.pre(3) | 2
