# GetWriteProtectionFlagSet Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IWriteProtection~GetWriteProtectionFlagSet.html

---

Checks what kind of a write protection was set.

Syntax

**C#**



bool GetWriteProtectionFlagSet( 

   IWriteProtection.WriteProtectionKind nKind

)

bool GetWriteProtectionFlagSet( 

   IWriteProtection.WriteProtectionKind nKind

)


#### Parameters

*nKind*
:   kind of a protection to test

#### Return Value

true : if given write protection reason is set

false : if given write protection reason is not set. Object still might be write protected
