# StartPosition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~StartPosition.html

---

start position of Interaction. The StartPosition is needed to calculate the current position while ortho mode is active or after input of length or angle the start position is automatically set after point input and before call of OnPoint after start of an interaction StartPosition is null

Syntax

**C#**



public virtual Position StartPosition {get; set;}

public:

virtual property Position^ StartPosition {

   Position^ get();

   void set (    Position^ value);

}

