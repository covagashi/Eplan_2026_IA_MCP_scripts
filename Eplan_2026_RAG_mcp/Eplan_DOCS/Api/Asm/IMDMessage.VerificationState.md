# IMDMessage.VerificationState

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.IMDMessage+VerificationState.html

---

The VerificationState determines the actual adjusted check type

Syntax

**C#**



public enum IMDMessage.VerificationState : System.Enum

public enum class IMDMessage.VerificationState : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **NoExecutionState** | 0 |  |
| **OfflineOnlyState** | 1 |  |

Remarks

The state must comply to the permission: only weaker states can be set dynamically. The state is normally set from scheme settings. Supported state values are:  
0 = NoExecutionState: The verification will be not executed in the next offline check run (certainly not in online mode).  
1 = OfflineOnlyState: The verification will be executed in an offline check run but not online.

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.MasterData.IMDMessage.VerificationState**
