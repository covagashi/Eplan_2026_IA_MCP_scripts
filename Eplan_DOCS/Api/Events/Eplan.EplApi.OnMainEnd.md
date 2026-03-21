# Eplan.EplApi.OnMainEnd

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.OnMainEnd.html

---

Sent when the Main End starts.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("Eplan.EplApi.OnMainEnd");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "On main end was called!", "OnMainEnd", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```