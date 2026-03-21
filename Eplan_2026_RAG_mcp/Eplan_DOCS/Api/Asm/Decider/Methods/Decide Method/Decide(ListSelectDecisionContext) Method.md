# Decide(ListSelectDecisionContext) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Decider~Decide(ListSelectDecisionContext).html

---

Decide shows a list select dialog.

Syntax

**C#**



public EnumDecisionReturn Decide( 

   ListSelectDecisionContext listSelectDecisionContext

)

public:

EnumDecisionReturn Decide( 

   ListSelectDecisionContext^ listSelectDecisionContext

)


#### Parameters

*listSelectDecisionContext*
:   A listselect context with all information

#### Return Value

The return value is EnumDecisionReturn::eOK or EnumDecisionReturn::eCancel.
