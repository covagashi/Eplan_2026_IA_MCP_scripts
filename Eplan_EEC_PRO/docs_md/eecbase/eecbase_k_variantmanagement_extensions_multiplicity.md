---
title: "Multiplicity"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecbase_k_variantmanagement_extensions_multiplicity.htm"
file: "eecbase_k_variantmanagement_extensions_multiplicity"
category: "eecbase"
---

# Multiplicity

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Multiplicity

The amount of instances of a library component to place on an extension point is specified by the Multiplicity value.

The value is specified as a range of values with the syntax <start value>..<end value> or as any value with the syntax *.

### [Example](javascript:void\(0\);)

It should not be possible to install up to four instances. | 
    
        0..4  
  
---|---  
Exactly two instances can be placed. | 
    
        2..2  
  
Any number of instances can be placed. | 
    
        *
