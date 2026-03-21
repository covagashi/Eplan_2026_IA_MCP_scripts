# VerificationState Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PartVerification~VerificationState.html

---

The VerificationState determines the actual adjusted check type whereas the permission determines what state is theoretically allowed at most.

Syntax

**C#**



public IVerificationBase.VerificationState VerificationState {get; set;}

public:

property IVerificationBase.VerificationState VerificationState {

   IVerificationBase.VerificationState get();

   void set (    IVerificationBase.VerificationState value);

}


Remarks

The state must comply to the permission: only weaker states can be set dynamically. The state is normally set from scheme settings (by the scheme dialog, for instance). supported state values for part verifications are:  
0 = NoExecutionState: The verification will be not executed in the next offline check run (certainly not in online mode).  
1 = OfflineOnlyState: The verification will be executed in an offline check run but not online.
