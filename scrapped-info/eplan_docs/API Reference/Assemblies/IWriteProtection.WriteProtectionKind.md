# IWriteProtection.WriteProtectionKind

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection+WriteProtectionKind.html

---

Detailed write protection states.

Syntax

**C#**



public enum IWriteProtection.WriteProtectionKind : System.Enum

public enum class IWriteProtection.WriteProtectionKind : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Design\_space** | 16 | Design space technology protection |
| **Disabled** | 1 | Write protection is on, but temporarily disabled for this object |
| **Manual** | 2 | Manual protection |
| **Planning** | 32 | Pre-planning protection |
| **Sub\_project\_mgmt** | 4 | Subproject management-related write protection |
| **Unset** | 0 | Write protection is not turned on |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.DataModel.IWriteProtection.WriteProtectionKind**
