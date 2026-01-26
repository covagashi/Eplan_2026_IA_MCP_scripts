# SetBinPaths Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Starteru~Eplan.EplApi.Starter.AssemblyResolver~SetBinPaths.html

---

Set the bin paths.

Syntax

**C#**



public void SetBinPaths( 

   string strPlatformBinPath,

   string strEplanBinPath

)

public:

void SetBinPaths( 

   String^ strPlatformBinPath,

   String^ strEplanBinPath

)


#### Parameters

*strPlatformBinPath*
:   The EPLAN platform bin path where all Eplan.EplApi.\*.dll are in. (And the W3Sharedu.dll)

*strEplanBinPath*
:   The EPLAN product variant bin path of the product variant w3u.exe.

Exceptions

| Exception | Description |
| --- | --- |
| [System.IO.DirectoryNotFoundException](#) | Thrown when directories cannot be found. |
| [System.ArgumentNullException](#) | Thrown when path is null. |
| [System.ArgumentException](#) | Thrown when path contains invalid characters such as ", <, >, or |. |
| [System.ArgumentException](#) | Thrown when the correct variant cannot be found. |
| [System.ArgumentException](#) | Thrown when no product variant path can be found. (with W3u.exe and install.xml). |
