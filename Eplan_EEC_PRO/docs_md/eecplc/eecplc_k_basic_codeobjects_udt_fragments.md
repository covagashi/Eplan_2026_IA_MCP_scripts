---
title: "UDT fragments, loops, and replace parameter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_basic_codeobjects_udt_fragments.htm"
file: "eecplc_k_basic_codeobjects_udt_fragments"
category: "eecplc"
---

# UDT fragments, loops, and replace parameter

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## UDT fragments, loops, and replace parameter

By means of the plug-socket design, fragments can be placed hierarchically below components of the type User-defined data type.

When the code is generated, the fragment contents are added by means of control structures (e.g., (*{Code}*)) into the code of the instance of the type User-defined data type.

Other control structures are also supported.

### Note

The improper use of control structures can cause the creation of invalid program elements.

### Note

The declaration area must be available as plain text in the resource of the component of the type User-defined Data Type so that control structures work correctly.

When reading in the resource belonging to the fragment, replace parameters (such as M8B_ReplaceParam_M8E) are automatically created. During generation of the codes these are replaced by the value of the parameter by the same name.

### Read more

     * [Replace parameters](eecplc_k_replace_parameter.htm)
