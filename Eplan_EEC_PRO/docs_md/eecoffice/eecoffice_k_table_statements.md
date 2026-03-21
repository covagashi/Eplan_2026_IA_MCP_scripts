---
title: "Control structures in tables"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_table_statements.htm"
file: "eecoffice_k_table_statements"
category: "eecoffice"
---

# Control structures in tables

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

Tables

## Control structures in tables

In addition to being used in continuous text, the control structures can also be used to create tables. When dealing with tables, only IF structures and the LOOP structure may be used. The IncludeDocument structure cannot be used in connection with a table.

What makes using control structures in tables unique is the position. For control structures, only the rows in the first column are evaluated. When dealing with multi-part structures, each part is contained in a separate row. All rows that contain a control structure are completely deleted during generation.
