---
title: "LOOP"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_table_statements_loop.htm"
file: "eecoffice_k_table_statements_loop"
category: "eecoffice"
---

# LOOP

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## LOOP

As in a continuous text, the control structure consists of the following parts: (*{LOOP: <Collection>}*) and (*{END_LOOP}*). Each of these is contained in a row of its own. All rows between these rows are replicated for each element in the collection.

If the content of a fragment is to be inserted, the (*{Content}*) structure can be included in a row of its own inside the Loop. The content of the target document is then copied to the content row for each fragment in the collection. This only works when each of the returned fragments contains one or more tables. The formatting, column width and style sheet of the table from the main document are applied to the extent possible. If the table from the fragment contains a column that deviates from the table of the control structure, it may not be possible to continue using the formatting.

Example:

The following table in a main document collects the rows from tables in subordinate fragment documents.

Item | Type | Designation  
---|---|---  
(*{LOOP:dos}*) |  |   
(*{Content}*) |  |   
(*{END_LOOP}*) |  |   
  
A table row from the fragment document:

#{Item} | #{Type} | #{Designator}  
---|---|---  
  
Result:

Item | Type | Designation  
---|---|---  
1 | Positionsensor_optical | Feeder.Insert.Magazine.Positionsensor_optical.Row_Tbl  
2 | Positionsensor_inductive | Feeder.Insert.Separator.Position_1.Row_Tbl  
3 | Positionsensor_inductive | Feeder.Insert.Separator.Position_2.Row_Tbl  
4 | Positionsensor_optical | Feeder.Test.BearingTester.Positionsensor_optical.Row_Tbl  
5 | Positionsensor_inductive | Feeder.Move.X_Axis.Position_1.Row_Tbl  
  
### Note

If a fragment contains only a single table (this holds as well for a single table row), the outcome of the insertion depends greatly on whether the control structure has been built into a table or a continuous text.

If the control structure is in a table, all fragments consisting of one or more table rows are attached as rows at the end of the same table. No new table is created; the existing table is merely expanded.

However, if the control structure is contained in a continuous text, each fragment is inserted separately into the target document as an independent table. No contiguous table is created.

This makes it possible not only to create contiguous tables, but also to create individual tables that partly differ in terms of formatting and content and to arrange them one below the other.
