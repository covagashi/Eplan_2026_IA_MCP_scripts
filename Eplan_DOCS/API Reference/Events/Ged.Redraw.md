# Ged.Redraw

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Ged.Redraw.html

---

If you send this event, a redraw of the graphical editor is forced.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("Ged.Redraw");

m_EventHandler.EplanEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "Ged.Redraw was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```