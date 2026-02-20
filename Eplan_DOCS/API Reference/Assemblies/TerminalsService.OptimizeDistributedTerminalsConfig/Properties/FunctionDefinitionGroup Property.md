# FunctionDefinitionGroup Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1453.html

---

An integer specifying a default [Eplan.EplApi.DataModel.FunctionDefinition.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition~Group.html) for distributed terminals. If part number of a distributed terminal is empty, the distributed terminal will get the specified function definition group. The default is 10.

Syntax

**C#**



public int FunctionDefinitionGroup {get; set;}

public:

property int FunctionDefinitionGroup {

   int get();

   void set (    int value);

}

