# VerificationPermission Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~VerificationPermission.html

---

The permission of a verification determines for what type of check the verification is enabled at most/ maximum.

Syntax

**C#**



public IVerificationBase.Permission VerificationPermission {get; set;}

public:

property IVerificationBase.Permission VerificationPermission {

   IVerificationBase.Permission get();

   void set (    IVerificationBase.Permission value);

}


Remarks

The permission should only initialized one-time (typically in the constructor in your verification class; default value is OnlineOfflinePermitted) and should not change during runtime. Supported permission values are: 0=NoExecutionPermitted: Verifications with "NoExecutionPermitted" are no 'real' verifications These so called "dummy verifications" are only used to delete simple project messages before an offline check run starts. 1=OfflineOnlyPermitted: Verification with this permission will only be executed in an offline check run. This verification is not allowed to be executed in online- state. Use this permission if your verification is very complex. 2=OnlineOfflinePermitted: If you choose this permission the verification will be executed in online- as well as in offline- mode. To avoid performance problems the verification should be fast. OnlineOfflinePermitted is the default. 3=RestrictivePermitted: Verifications with this permission will be executed in online- as well as in offline-mode(so the verification should be fast). In the online state a dialog will be shown and the change, that generated the project message will be canceled. In the offline state the verification will be executed but without the undo.
