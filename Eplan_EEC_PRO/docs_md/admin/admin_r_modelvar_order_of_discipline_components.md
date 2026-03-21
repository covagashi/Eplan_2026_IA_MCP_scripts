---
title: "Parameter name for the sort order"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_modelvar_order_of_discipline_components.htm"
file: "admin_r_modelvar_order_of_discipline_components"
category: "admin"
---

# Parameter name for the sort order

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter name for the sort order

Path to model variable:

Model Variables > Disciplines

Specify the name of a parameter. Add this parameter to the discipline components. The value of the parameter in the discipline components defines the order in which the components of the discipline structure are sorted. The sorting is in ascending order. The directly subordinated discipline components of a parent discipline component are sorted. If subordinate discipline components with and without sorting parameter are found, then discipline components without parameter are sorted to the end (they have implicitly an infinite parameter value). The parameter is determined in the mechatronic structure before inserting the discipline component into the discipline structure. Formulas which determine the value in the discipline structure (e.g. dc, rdc, dos, etc.) cannot work.
