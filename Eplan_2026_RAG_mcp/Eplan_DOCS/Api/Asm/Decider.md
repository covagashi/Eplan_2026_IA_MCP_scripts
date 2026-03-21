# Decider

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider.html

---

This class implements the standard EPLAN decider dialog.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.Base.Decider**

Syntax

**C#**



public class Decider

public ref class Decider


Example

Example of using Decider class:

- [c#](#i-tab-content-edf133b9-c02d-49d3-8544-e60a41509139)

```
Decider eDecision = new Decider();

EnumDecisionReturn eAnswer = eDecision.Decide(eOkCancelDecision, "Show some dialog text", "Eplan Decider", eOK, eOK);

if (eAnswer == eOK)

{

    // Do your work

}
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Decider Constructor](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~_ctor.html) | Create a new Decider Object. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Decide](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~Decide.html) | Overloaded. Decide shows a list select dialog. |
| Public Method | [Dispose](Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~Dispose().html) | Destructor for deterministic finalization of Decider object. |


