# HasOption Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.License~HasOption.html

---

Is used to determine whether a license for this option exists in the system and if it is available.

Syntax

**C#**



public bool HasOption( 

   LicenseOptions eOption

)

public:

bool HasOption( 

   LicenseOptions eOption

)


#### Parameters

*eOption*
:   Determines whether a license is available on the system for this licensing option.

#### Return Value

true: This options is licensed on the system. false: This options is not licensed on the system.
