# Eplan.EplApi.OnLoadWorkspace

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.OnLoadWorkspace.html

---

Sent after changing the workspace to recreate the menu items in the ribbon bar.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("Eplan.EplApi.OnLoadWorkspace");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "OnLoadWorkspace was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```