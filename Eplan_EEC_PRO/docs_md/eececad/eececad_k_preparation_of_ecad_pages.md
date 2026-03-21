---
title: "Modularization of ECAD pages"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_preparation_of_ecad_pages.htm"
file: "eececad_k_preparation_of_ecad_pages"
category: "eececad"
---

# Modularization of ECAD pages

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Modularization of ECAD pages

To modularize ECAD pages, it is essential that two tasks be carried out. First, the entire pages are broken down into meaningful partial circuits in the form of window macros. Second, the generated values are set up as parameters. Eplan Electric P8 uses the placeholder object to define variables. The variables thus defined become the parameters of the ECAD object when the resource is imported. During the generation of the schematic, they can then be calculated from within EEC and filled with concrete values.

Parameters can be assigned for many elements of the schematic, for example, for terminal designations, structure identifiers/device tags, technical characteristics or page numbers.

In practice defining multiple placeholder objects if many objects are to be parameterized has to proved to be successful. The parameters are read out jointly in EEC. Thus, nothing changes in EEC if several or only one placeholder object is used.

Rule:

The syntax #<Parametername> may be used only for the definition of the plugs and sockets, because they are not assigned to any placeholder object. All other parameters in the placeholder objects use the following syntax by default in Eplan Electric P8:

<Parameter name>

Text objects:

Further properties of a parameter can be entered in text objects, but they will be evaluated only if the parameter does not yet exist up to the time the document is read in. **Type** , **Default value** , and **Comment** can be entered in the sequence.

The syntax then follows this pattern:
    
        <Type:Parameter name=Default value//Comment>

Example:
    
        <String:Location=St01Insert//MountingLocation>

This means that Type, Default value, and Comment are independent of each other, and each is optional.

When a resource is assigned or edited and then saved, the content is read in and the parameter sequences are evaluated. Then, the ECAD discipline determines the parameters that already exist and which parameters have yet to be created. In the latter case, the appropriate parameters are created, while taking all of the entries into account.

In the process, missing entries for optional information, i.e. "Type", "Default value", and "Comment", are replaced by the following values:

Statement | Value  
---|---  
Type | String  
Default value | <empty>  
Comment | <empty>  
  
If a new parameter has been created, or if a parameter already exists with the stated name, it will be assigned to the text object whose resource has just been read in.
