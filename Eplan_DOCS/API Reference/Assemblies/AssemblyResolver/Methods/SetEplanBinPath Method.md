# SetEplanBinPath Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~SetEplanBinPath.html

---

Set the EPLAN product variant bin path. Note: This path exists only once. Changing it will influence the application. The EPLAN platform path (with the API DLLs) is set automatically.

Syntax

**C#**



public void SetEplanBinPath( 

   string strEplanBinPath

)

public:

void SetEplanBinPath( 

   String^ strEplanBinPath

)


#### Parameters

*strEplanBinPath*
:   The EPLAN product variant bin path where the w3u.exe of your product variant is in (p.e. "Electric P8")

Exceptions

| Exception | Description |
| --- | --- |
| [System.IO.DirectoryNotFoundException](#) | Thrown when directory cannot be found. |
| [System.ArgumentNullException](#) | Thrown when path is null. |
| [System.ArgumentException](#) | Thrown when path contains invalid characters such as ", <, >, or |. |
| [System.ArgumentException](#) | Thrown when no platform path can be found (with API DLLs) |

Remarks

The EPLAN product variant bin path is the bin path with the w3u.exe you start normally.
