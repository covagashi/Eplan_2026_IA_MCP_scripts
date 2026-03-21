---
title: "Symbol lists"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_symbollist.htm"
file: "eecplc_k_symbollist"
category: "eecplc"
---

# Symbol lists

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Symbol lists

The structure of the symbol lists usually exhibits a very simple hierarchy. It consists of at least two levels: a body or head object and the lines. In some systems, blocks for the various signal types are defined in the symbol list. An additional level (called a section, for example) can also be inserted into the list between the other two.

The body contains only information that never appears in a symbol list more than once, e.g. a caption, and is very often completely empty. The body also includes one or more lines that contain the formula for listing all of the lines. The formula is formulated in a way that closely resembles the text discipline.

For each data field, the line contains a parameter that must be included on the symbol list on a single line. Examples of these parameters include: absolute address, symbolic name, data type and comment.

Parameters that are used in modeling the symbol lists can contain several specific tokens and prefixes. The values of the tokens are set as model variables in the PLC group. The following screenshot indicates the default values.

The tokens are valid for the entire PLC discipline and can be used anywhere in the resource filesâand so not only in the symbol lists. There are two ways to define parameters directly in the resource: via parameter definition with data-type declaration or via so-called replace variables. The functionality of the replace variables is similar to that of the variables in resources for the text discipline.

Comments for the S7 assignment list can be calculated with the following parameters (see Model > Model variables > Discipline > PLC > STEP 7 > SIMATIC):

Parameter | Usage  
---|---  
Comment Parameter Name (default = SimaticComment) | This parameter is used for all types of function blocks. In the case of FBs this parameter contains the comment of the DB instance.  
FB Comment Parameter Name  
(default = FBSimaticComment) | This parameter contains the comment for the FB and is only taken into account when creating FBs.  
  
When creating assignment-list comments, all available comments are evaluated in the following order:

    1. Comment in the parameter.
    2. Project-component comment.
    3. Library-component comment.

When creating assignment-list comments, these three positions are searched. If no comment entry is available in one of the positions, a search is conducted for the comment in the next position. If no comment is found in any position, the comment in the S7 assignment list remains empty.
