# SetBinPathsWithAppMod Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~SetBinPathsWithAppMod.html

---

Set the EPLAN platform bin path. The EPLAN product variant path will be searched with the help of the applicationModifier.

Syntax

**C#**



public void SetBinPathsWithAppMod( 

   string strPlatformBinPath,

   string strAppMod

)

public:

void SetBinPathsWithAppMod( 

   String^ strPlatformBinPath,

   String^ strAppMod

)


#### Parameters

*strPlatformBinPath*
:   The path where all Eplan.EplApi.\*.dll are in. (And the W3Sharedu.dll)

*strAppMod*
:   The wanted ApplicationModifer

Exceptions

| Exception | Description |
| --- | --- |
| [System.IO.DirectoryNotFoundException](#) | Thrown when directory cannot be found. |
| [System.ArgumentNullException](#) | Thrown when path is null. |
| [System.ArgumentException](#) | Thrown when path contains invalid characters such as ", <, >, or |. |
| [System.ArgumentException](#) | Thrown when the correct product variant cannot be found. |
| [System.ArgumentException](#) | Thrown when no product variant path can be found (with W3u.exe and install.xml). |

Remarks

The EPLAN platform bin path is the bin path with all Eplan.EplApi.\*.dll and W3Sharedu.dll This function searches the correct product variant. This may be slow.
