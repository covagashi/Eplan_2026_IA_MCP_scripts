# PlcService.ImportMatch

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService+ImportMatch.html

---

Matching options for PLC data import.

Syntax

**C#**



public enum PlcService.ImportMatch : System.Enum

public enum class PlcService.ImportMatch : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Id** | 0 | Match by internal object ids. |
| **Name** | 1 | Match by identifying names. Note: in this case, a comparison dialog may be displayed for the user to individually selecting some function to update. |
| **Nothing** | 2 | Don't match. Create new functions for all imported objects. |

Remarks

The import process tries to match imported objects with those existing in the project. Based on the option selected, the matching may be performed by internal object ids or by objects' identifying names. If an imported object is matched with an existing function, properties of the existing function will be updated whereas for unmatched imported objects, new functions will be created in the project.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.HEServices.PlcService.ImportMatch**
