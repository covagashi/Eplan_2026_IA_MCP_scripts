# Page.ConnectionDirty

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Page.ConnectionDirty.html

---

Sent when a page gets dirty.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("Page.ConnectionDirty");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "Page.ConnectionDirty was called!", "Title", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```