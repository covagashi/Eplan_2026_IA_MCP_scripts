# IVerificationBase.VerificationState

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerificationBase+VerificationState.html

---

The VerificationState determines the actual adjusted check type whereas the permission determines what state is theoretically allowed at most.

Syntax

**C#**



public enum IVerificationBase.VerificationState : System.Enum

public enum class IVerificationBase.VerificationState : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **NoExecutionState** | 0 |  |
| **OfflineOnlyState** | 1 |  |
| **OnlineOfflineState** | 2 |  |
| **RestrictiveState** | 3 |  |

Remarks

The state must comply to the permission: only weaker states can be set dynamically. The state is normally set from scheme settings (by the scheme dialog, for instance). Supported state values are: 0=NoExecutionState: The verification will be not executed in the next offline check run (certainly not in online mode). 1=OfflineOnlyState: The verification will be executed in an offline check run but not online. 2=OnlineOfflineState: The verification will be executed in an offline check run as well as online. "Online" means, that every time an undo step opens (an object is changed, a new object is inserted or an object is deleted), the verification will be executed. OnlineOfflineState is the default. 3=RestrictiveState: The verification will be executed in an offline check run as well as online. Additionally in online mode and if the verification announces an error, the last change will be canceled. This state can only be set if the permission of the verification was initialized with RestrictivePermitted.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.IVerificationBase.VerificationState**
