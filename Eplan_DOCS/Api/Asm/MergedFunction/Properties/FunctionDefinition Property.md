# FunctionDefinition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~FunctionDefinition.html

---

Returns the [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the merged function.

Syntax

**C#**



public virtual FunctionDefinition FunctionDefinition {get; set;}

public:

virtual property FunctionDefinition^ FunctionDefinition {

   FunctionDefinition^ get();

   void set (    FunctionDefinition^ value);

}


#### Property Value

Merged function's [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) or NULL if merged function doesn't have a valid FunctionDefinition.
