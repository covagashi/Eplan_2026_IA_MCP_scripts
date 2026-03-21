# GetLicenseModules Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~GetLicenseModules.html

---

Syntax

**C#**



public void GetLicenseModules( 

   ref Dictionary<LicenseOptions,bool> LicenseModulesDic

)

public:

void GetLicenseModules( 

   Dictionary<LicenseOptions,bool>^% LicenseModulesDic

)


#### Parameters

*LicenseModulesDic*
:   A Dictionary of license modules (output parameter).

Remarks

After executing this method, the LicenseModulesDic parameter contains a dictionary of license modules. The key is the license option of the module, the value is the state whether the module license is available or not.
