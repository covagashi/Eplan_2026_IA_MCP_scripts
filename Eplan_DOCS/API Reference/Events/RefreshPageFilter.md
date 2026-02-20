# RefreshPageFilter

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/RefreshPageFilter.html

---

Sent when page filter has been changed. This event will refresh navigator data.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("RefreshPageFilter");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "RefreshPageFilter was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```