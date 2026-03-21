# NCSettingsMachineTools.Redraw

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/NCSettingsMachineTools.Redraw.html

---

If you send this event, a redraw of the NC Machine Tools settings tab is forced.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("NCSettingsMachineTools.Redraw");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "NCSettingsMachineTools.Redraw was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```