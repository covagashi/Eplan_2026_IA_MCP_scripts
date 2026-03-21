---
title: "-xms"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_xms.htm"
file: "admin_r_vmargs_xms"
category: "admin"
---

# -xms

This functionality is only available for certain module packages. [Info / Copyright](license.htm)  
  
You are here: 

## -xms

EEC argument |  Usage  
---|---  
-xms=<value>m |  Optional  
**Annotation**  
RAM that is made available to the application by the operating system initially. It is measured in megabytes (m). The Java VM requests new heap memory from the operating system as needed. Due to the growing RAM requirements during booting, multiples of additional RAM are reserved. An acceleration of the boot-up is possible by setting the initial RAM directly to a meaningful initial value. The initial value should be in a range that corresponds to the application after booting (see Task Manager, memory usage of javaw.exe), that is, around 70 MB. When it comes to optimizing booting times, it should be noted that the effect of this argument, compared to the âclean argument, is negligible.
