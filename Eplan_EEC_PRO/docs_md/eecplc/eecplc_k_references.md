---
title: "References"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_references.htm"
file: "eecplc_k_references"
category: "eecplc"
---

# References

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## References

In the library, a reference component can now be created by means of the menu (New > CoDeSys > Source > Reference). For this, a parameter will be created (by hand) that contains a reference to another element. The name of the parameter that contains this reference is created by means of the model variables (Disciplines > PLC > CoDeSys > CoDeSys V3 > Parameter name from reference target).

To ensure that a POU is entered, the parameter (created by hand) should be of type ProgramOrganisationUnit.

For each formula, a reference to another element can now be entered in the parameter. This can be both a mechatronic (discipline) component and also a component in the discipline structure. In the first case (mechatronic component), for the code generation, the matching component is automatically searched for in the discipline structure.

Example formula reference (mechatronics):
    
        =mroot.rmos('PLCTests_CoDeSysV3_Bibliothek.CoDeSys.Resource.Bausteine.POUs.M8B_PouName_M8E').first

Example formula reference (discipline)
    
        =droot.rdos('PLCTests_CoDeSysV3_Bibliothek.CoDeSys.Resource.Bausteine.POUs.M8B_PouName_M8E').first

Currently, references can be made only to programs (super class SourceProgram) and actions (super class Action).

By means of a network socket (FBD,KOP), a new block can now be created automatically with a call.

Example SoMachine source:

Example discipline structure ("FBD_Reference" points to "ReplacedName"):

Example result (in SoMachine)

Because sockets for POUs with the language ST have not yet been implemented, the call must also be inserted by hand (by means of LOOP). However, here, the reference element is also called correctly (and not the reference component itself).

Example SoMachine source:

Example discipline structure ("FBD_Reference" points to "ReplacedName"):

Example result (in SoMachine):
