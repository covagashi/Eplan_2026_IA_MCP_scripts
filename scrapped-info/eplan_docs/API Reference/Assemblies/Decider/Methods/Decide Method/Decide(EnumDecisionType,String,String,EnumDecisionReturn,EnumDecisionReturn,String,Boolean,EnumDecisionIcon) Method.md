# Decide(EnumDecisionType,String,String,EnumDecisionReturn,EnumDecisionReturn,String,Boolean,EnumDecisionIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic3.html

---

decide shows the dialog. When the application id in quiet mode, the batch decision is returned.

Syntax

**C#**



public EnumDecisionReturn Decide( 

   EnumDecisionType type,

   string strText,

   string strTitle,

   EnumDecisionReturn eDefaultDecision,

   EnumDecisionReturn eBatchDecision,

   string strDecisionId,

   bool bShowCheckBox,

   EnumDecisionIcon eIcon

)

public:

EnumDecisionReturn Decide( 

   EnumDecisionType type,

   String^ strText,

   String^ strTitle,

   EnumDecisionReturn eDefaultDecision,

   EnumDecisionReturn eBatchDecision,

   String^ strDecisionId,

   bool bShowCheckBox,

   EnumDecisionIcon eIcon

)


#### Parameters

*type*
:   the type of the decider

*strText*
:   The text to show in the window.

*strTitle*
:   The title of the window

*eDefaultDecision*
:   A default decision, this one is preselected in the dialog.

*eBatchDecision*
:   The decision taken when no dialogs are allowed. used in quiet mode.

*strDecisionId*
:   The decision id. A unique text to identify this dialog. Needed when the checkbox should be shown.

*bShowCheckBox*
:   Show a checkbox like "do not show this decision again". Then the batch decision is returned the next time.

*eIcon*
:   The icon displayed on the dialog.

#### Return Value

The return value includes the pressed button or error.
