# Renumber.Enums.TerminalsWithAlphabeticalCharacters

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber+Enums+TerminalsWithAlphabeticalCharacters.html

---

Parameter enum how terminals or pins with alphabetical elements in the designation should be numbered: .

Syntax

**C#**



public enum Renumber.Enums.TerminalsWithAlphabeticalCharacters : System.Enum

public enum class Renumber.Enums.TerminalsWithAlphabeticalCharacters : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **DontModify** | 0 | Terminals or pins with alphabetical elements in the designation are ignored during numbering. |
| **KeepAlphabeticalElements** | 1 | The alphabetical elements of the terminal or pin designation are retained. The first numeric elements are renumbered. If the designation only has alphabetical elements, the old designation is attached to the new numbering. Sequential terminals with different counters but the same numerical component receive the same numerical component in the counter even after the numbering. |
| **Number** | 2 | All terminals / pins are renumbered. In doing so, the old designation is overwritten |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Renumber.Enums.TerminalsWithAlphabeticalCharacters**
