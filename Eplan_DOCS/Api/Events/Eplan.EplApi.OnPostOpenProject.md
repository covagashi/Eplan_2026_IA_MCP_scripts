# Eplan.EplApi.OnPostOpenProject

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.OnPostOpenProject.html

---

Project management: Sent after opening a project.

#### **Parameter**

This parameter contains the name of the project being opened. Parameter type for API use is IEventParameter.

**Example**

```
m_EventHandler = new EventHandler("Eplan.EplApi.OnPostOpenProject");

m_EventHandler.EplanEvent += delegate (IEventParameter parameter)

{

    new Decider().Decide(EnumDecisionType.eOkDecision, " Project " + new EventParameterString(parameter).String + " was open!", "OnPostOpenProject", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```