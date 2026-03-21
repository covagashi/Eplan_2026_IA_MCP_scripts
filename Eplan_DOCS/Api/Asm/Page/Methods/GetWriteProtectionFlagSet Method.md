# GetWriteProtectionFlagSet Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~GetWriteProtectionFlagSet.html

---

Checks if a specific write protection kind was set.

Syntax

**C#**



public virtual bool GetWriteProtectionFlagSet( 

   IWriteProtection.WriteProtectionKind nKind

)

public:

virtual bool GetWriteProtectionFlagSet( 

   IWriteProtection.WriteProtectionKind nKind

)


#### Parameters

*nKind*
:   kind of plotection to test

#### Return Value

true : if given write protection reason is set

false : if given write protection reason is not set. Object sill might be write protected
