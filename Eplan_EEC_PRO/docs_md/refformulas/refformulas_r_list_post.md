---
title: "post(Object obj)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_list_post.htm"
file: "refformulas_r_list_post"
category: "refformulas"
---

# post(Object obj)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  post(Object obj) Methods for list Returns the successor to object obj. post(Object obj)  
---  
Argument | Object | obj | Object for which the successor is sought.  
Return value | Object |  Successor to obj. If obj is the last object of the list, <null> is returned. If obj is not included in the list, <null> is also returned.  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=List{1,2,3,4}.post(3) | 4
