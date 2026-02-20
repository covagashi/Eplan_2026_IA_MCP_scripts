# IMessage.ProjectMessageCreationType

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+ProjectMessageCreationType.html

---

Methods by which a project message have been created.

Syntax

**C#**



public enum IMessage.ProjectMessageCreationType : System.Enum

public enum class IMessage.ProjectMessageCreationType : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **Explicit** | 3 | Message was output via another module and thus created "outside" of the message management (e.g., in the case of automatic cable generation, or when addressing PLC inputs and /or outputs). These module-specific messages are displayed together with the "normal" project check messages in the message management dialog |
| **Offline** | 2 | Message was output during project checking. In could be either GUI dialog 'Check project', API action 'check' or Check.VertifyProject method. |
| **Online** | 1 | Message was generated implicitly during project edition |
| **Undefined** | 0 | Available for older projects that did not have the types of check available at the time, or for the ones which no current project check has yet been performed |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.EServices.IMessage.ProjectMessageCreationType**
