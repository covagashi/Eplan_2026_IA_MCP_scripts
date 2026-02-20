# Backup.Amount

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Backup+Amount.html

---

Scope of data backup

Syntax

**C#**



public enum Backup.Amount : System.Enum

public enum class Backup.Amount : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **All** | 0 | The entire project directory is backed up. |
| **Min** | 1 | Only the database files required to restore the project are backed up; redundant database files are ignored. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.Backup.Amount**
