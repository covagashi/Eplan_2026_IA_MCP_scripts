# FunctionDefinition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~FunctionDefinition.html

---

Returns the [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Connection.

Syntax

**C#**



public virtual FunctionDefinition FunctionDefinition {get; set;}

public:

virtual property FunctionDefinition^ FunctionDefinition {

   FunctionDefinition^ get();

   void set (    FunctionDefinition^ value);

}


#### Property Value

Connections's [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) or NULL if Connection doesn't has a FunctionDefinition.
