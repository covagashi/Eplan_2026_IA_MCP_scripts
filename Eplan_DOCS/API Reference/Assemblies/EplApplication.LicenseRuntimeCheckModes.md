# EplApplication.LicenseRuntimeCheckModes

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Systemu~Eplan.EplApi.System.EplApplication+LicenseRuntimeCheckModes.html

---

License runtime check modes

Syntax

**C#**



public enum EplApplication.LicenseRuntimeCheckModes : System.Enum

public enum class EplApplication.LicenseRuntimeCheckModes : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Cancel** | 1 | Cancel the license runtime check and free license. After a license is freed, each license call made will fail. |
| **TryCancel** | 0 | Try or cancel the license runtime check. |

Remarks

These values will be returned from the license system to inform client application which possibilities are available: - TryCancel: There are two possibilities. try or cancel the license runtime check. The license runtime check callback Handler can return following values: - LicenseRuntimeCheckMode::Cancel : cancel license runtime check and free license. - LicenseRuntimeCheckMode::Retry : retry license runtime check again. - Cancel: There is only one possibility: cancel the license runtime check. The license runtime check callback Handler can return only following value: - LicenseRuntimeCheckMode::Cancel : cancel license runtime check and free license. If other values are returned, they will be considered as Cancel.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.System.EplApplication.LicenseRuntimeCheckModes**
