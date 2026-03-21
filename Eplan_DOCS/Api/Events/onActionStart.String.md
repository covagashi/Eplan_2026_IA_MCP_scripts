# onActionStart.String.*

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/onActionStart.String._star_.html

---

Send before the start of any action.

#### **Parameter**

Has no event parameter.

**Example**

```
m_EventHandler = new EventHandler("onActionStart.String.*");

m_EventHandler.EplanNameEvent += delegate (IEventParameter parameter, string strNameOfEvent)

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "Event " + strNameOfEvent + " will be called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

m_EventHandler = new EventHandler("onActionStart.String.XPartsManagementStart");

m_EventHandler.EplanNameEvent += delegate

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "Action XPartsManagementStart will be called!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

};

```