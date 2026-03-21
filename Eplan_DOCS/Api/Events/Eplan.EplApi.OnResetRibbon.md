# Eplan.EplApi.OnResetRibbon

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.OnResetRibbon.html

---

Sent when the customize ribbon dialog is closed with OK and the reset button was pressed before.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("Eplan.EplApi.OnResetRibbon");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "OnResetRibbon was called!", "Title", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```