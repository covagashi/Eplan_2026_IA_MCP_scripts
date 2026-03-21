---
title: "-xmx"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_xmx.htm"
file: "admin_r_vmargs_xmx"
category: "admin"
---

# -xmx

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -xmx

EEC argument |  Usage  
---|---  
-xmx=<value>m |  Optional  
**Annotation**  
Maximum RAM that is made available to the application by the operating system. It is measured in megabytes (m). The value set should not exceed 50% of the physically available memory. For example, 256 or 1024 Standard setting for Stand-alone and Worker installation:
    
        -Xmx1536m

Standard setting for Job Server installation:
    
        -Xmx1792m
