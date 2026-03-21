---
title: "-xss"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_xss.htm"
file: "admin_r_vmargs_xss"
category: "admin"
---

# -xss

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -xss

EEC argument |  Usage  
---|---  
-xss=<Wert>k|m |  Optional  
**Annotation**  
Stack, which is available for the processing of the most instructions and also results of operations. The value is given in kilobyte (k) or megabyte (m). This specification is not necessary by default. If stack overflow exceptions are thrown, this could be an indicator for too low specification of the xss value. This specification is located below the specification for the operation memory (-Xmx). Example for Web EEC: -Xss1m Example for a model with excessive nesting depth in formulas: -Xss2m
