# FileSelectDecisionContext Constructor(String,EnumDecisionReturn)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~_ctor(String,EnumDecisionReturn).html

---

Create a new FileSelectDecisionContext Object.

Syntax

**C#**



public FileSelectDecisionContext( 

   string strDecisionId,

   EnumDecisionReturn eDefaultDecision

)

public:

FileSelectDecisionContext( 

   String^ strDecisionId,

   EnumDecisionReturn eDefaultDecision

)


#### Parameters

*strDecisionId*
:   The identifier for this fileselect. Use a unique one and the fileselect dialog remembers the user input and dialog position for the next time.

*eDefaultDecision*
:   A default decision, this one is preselected in the dialog.
