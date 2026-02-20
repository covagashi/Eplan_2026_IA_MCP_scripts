# Eplan.EplApi.OnMainStart

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.OnMainStart.html

---

Sent when the Main Start is done. This is when a mainframe is available. The event is not sent when the application is started in offline mode or to execute an action.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("Eplan.EplApi.OnMainStart");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "On main start was called!", "OnMainStart", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```