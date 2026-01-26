# License

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License.html

---

Class for querying Eplan licensing options ([LicenseOptions](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.LicenseOptions.html)).

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.ApplicationFramework.License**

Syntax

**C#**



public class License

public ref class License

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [License Constructor](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~_ctor.html) |  |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DongleNumber](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~DongleNumber.html) | Get the dongle number |
| Public Property | [Type](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~Type.html) | Gets license type: local, remote (network) or borrowed. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~Dispose().html) | Destructor for deterministic finalization of License object. |
| Public Method | [GetLicenseModules](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~GetLicenseModules.html) |  |
| Public Method | [HasOption](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~HasOption.html) | Is used to determine whether a license for this option exists in the system and if it is available. |
| Public Method | [LockOption](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~LockOption.html) | Assigns a license to an option on the system, i.e., a license for this option is deducted. If all available licenses for this option are already in use, the function fails. An option is used until the program is exited. |


