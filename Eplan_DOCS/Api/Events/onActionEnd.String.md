# onActionEnd.String.*

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/onActionEnd.String._star_.html

---

Sent after the end of any action.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("onActionEnd.String.*");

m_EventHandler.EplanEvent += delegate (IEventParameter parameter)

{

    new Decider().Decide(EnumDecisionType.eOkDecision, " Action " + new EventParameterString(parameter).String + " was called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

m_EventHandler = new EventHandler("onActionEnd.String.XPartsManagementStart");

m_EventHandler.EplanNameEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, " Action XPartsManagementStart was be called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```