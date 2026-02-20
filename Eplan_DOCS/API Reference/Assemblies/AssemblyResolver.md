# AssemblyResolver

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver.html

---

The AssemblyResolver class does everything needed to resolve the EPLAN API DLLs. When a bin path is specified, all EPLAN API DLLs inside can be loaded.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Starter.AssemblyResolver**

Syntax

**C#**



public class AssemblyResolver

public ref class AssemblyResolver

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [AssemblyResolver Constructor](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~_ctor.html) | Create one AssemblyResolver. This will automatically add an AssemblyResolve Event Handler for this domain. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [GetEplanBinPath](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~GetEplanBinPath.html) | Get the EPLAN product variant bin path. The EPLAN product variant bin path where the w3u.exe of your product variant is in (p.e. "Electric P8") |
| Public Method | [GetPlatformBinPath](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~GetPlatformBinPath.html) | Get the EPLAN platform bin path. The bin path where the w3Sharedu.dll is in and all your API DLLs |
| Public Method | [PinToEplan](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~PinToEplan.html) | Pin an offline application to an EPLAN application. When the EPLAN product variant bin path is known, an Offline Application using the EPLAN API DLL can be pinned to this version. This means all referenced EPLAN API DLLs will be loaded. Note: For already loaded linked DLLs the AssemblyResolve event is not fired. |
| Public Method | [SetBinPaths](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~SetBinPaths.html) | Set the bin paths. |
| Public Method | [SetBinPathsWithAppMod](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~SetBinPathsWithAppMod.html) | Set the EPLAN platform bin path. The EPLAN product variant path will be searched with the help of the applicationModifier. |
| Public Method | [SetEplanBinPath](Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~SetEplanBinPath.html) | Set the EPLAN product variant bin path. Note: This path exists only once. Changing it will influence the application. The EPLAN platform path (with the API DLLs) is set automatically. |


