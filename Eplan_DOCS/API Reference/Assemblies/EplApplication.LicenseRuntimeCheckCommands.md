# EplApplication.LicenseRuntimeCheckCommands

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication+LicenseRuntimeCheckCommands.html

---

License runtime check commands to return to the license system. These values are returned from the License runtime check callback Handler to notify the license system what to do.

Syntax

**C#**



public enum EplApplication.LicenseRuntimeCheckCommands : System.Enum

public enum class EplApplication.LicenseRuntimeCheckCommands : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Cancel** | 2 | Cancel license runtime check and free license. After a license is freed, each license call made will fail. |
| **Retry** | 4 | Retry license runtime check. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.System.EplApplication.LicenseRuntimeCheckCommands**
