# Eplan.EplApi.OnUserPreCloseProject

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.OnUserPreCloseProject.html

---

Project management: Sent before closing a project.

#### **Parameter**

This parameter contains the name of the project to close. Parameter type for API use is IEventParameter.

**Example**

```
m_EventHandler = new EventHandler("Eplan.EplApi.OnUserPreCloseProject");

m_EventHandler.EplanEvent += delegate (IEventParameter parameter)

{

    new Decider().Decide(EnumDecisionType.eOkDecision, " Project " + new EventParameterString(parameter).String + " will be closed!", "OnUserPreCloseProject", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```