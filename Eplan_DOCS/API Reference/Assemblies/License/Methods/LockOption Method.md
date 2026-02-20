# LockOption Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~LockOption.html

---

Assigns a license to an option on the system, i.e., a license for this option is deducted. If all available licenses for this option are already in use, the function fails. An option is used until the program is exited.

Syntax

**C#**



public bool LockOption( 

   LicenseOptions eOption

)

public:

bool LockOption( 

   LicenseOptions eOption

)


#### Parameters

*eOption*
:   A license is assigned to this option.

#### Return Value

true: A license has been successfully assigned to this option. false: No license has been assigned to this option.
