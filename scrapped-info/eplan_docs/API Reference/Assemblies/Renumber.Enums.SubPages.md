# Renumber.Enums.SubPages

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+SubPages.html

---

Parameter enum for pages numbering.

Syntax

**C#**



public enum Renumber.Enums.SubPages : System.Enum

public enum class Renumber.Enums.SubPages : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **ConsecutiveNumbering** | 1 | Existing subpages are renumbered using the starting value "1" and an increment of "1". At every change of the main page, the subpage numbering begins again from "1". The subpage numbering follows the project settings defined in the project setting "Characters for subpages". |
| **ConvertIntoMainPages** | 2 | Subpages are converted to main pages and renumbered. |
| **Retain** | 0 | Existing subpages are adopted unchanged into the target page. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Renumber.Enums.SubPages**
