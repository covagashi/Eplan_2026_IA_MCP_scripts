# FunctionDefinition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPoint~FunctionDefinition.html

---

Returns the [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Function.

Syntax

**C#**



public override FunctionDefinition FunctionDefinition {get; set;}

public:

property FunctionDefinition^ FunctionDefinition {

   FunctionDefinition^ get() override;

   void set (    FunctionDefinition^ value) override;

}


#### Property Value

Function's [Function.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~FunctionDefinition.html) or NULL if Function doesn't have FunctionDefinition.
