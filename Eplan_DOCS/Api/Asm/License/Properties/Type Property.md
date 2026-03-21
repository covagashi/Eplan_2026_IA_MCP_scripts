# Type Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~Type.html

---

Gets license type: local, remote (network) or borrowed.

Syntax

**C#**



public LicenseType Type {get;}

public:

property LicenseType Type {

   LicenseType get();

}


#### Property Value

Type of the license currently in use.

Remarks

If licensing is not initialized no license type will be returned. In this case the value LicenseType.NoLicense will be returned.
