---
title: "CoDeSys fragments"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_basic_codeobjects_codesys_fragments.htm"
file: "eecplc_k_basic_codeobjects_codesys_fragments"
category: "eecplc"
---

# CoDeSys fragments

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## CoDeSys fragments

The resources of CoDeSys fragments must have the following structure:

### [Example code](javascript:void\(0\);)
    
        FRAGMENT <FragmentName>
    <Variablendeklaration>
    (*@END_DECLARATION*)
    <FragmentCode>
    END_FRAGMENT

     * FragmentName:

When you create a new discipline component with this resource, the entry for FragmentName is automatically entered in the Name field.

     * Variable declaration (optional):

An area for the variable declarations is located below the fragment name. The variable declarations must not contain any comments. The declared variables can be inserted into other components via control structures (for example (*{TempVariableDeclaration}*)).

     * FragmentCode (optional):

Insert the fragment code between the lines (*@END_DECLARATION*) and END_Fragment. The complete code can be inserted into other components via the control structure (*{Code}*).

### [Example code for the contents of a fragment resource](javascript:void\(0\);)
    
        FRAGMENT CallingFragment
    VAR
    	In1:BOOL;
    	In2:BOOL;
    END_VAR
    (* @END_DECLARATION*)
    This text can be inserted as code
    END_FRAGMENT
