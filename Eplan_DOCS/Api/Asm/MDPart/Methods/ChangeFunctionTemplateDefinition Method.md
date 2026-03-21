# ChangeFunctionTemplateDefinition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~ChangeFunctionTemplateDefinition.html

---

Changes function definition of a function template position

Syntax

**C#**



public void ChangeFunctionTemplateDefinition( 

   ref MDFunctionTemplatePosition functionTemplatePosition,

   FunctionCategory category,

   short group,

   short id

)

public:

void ChangeFunctionTemplateDefinition( 

   MDFunctionTemplatePosition^% functionTemplatePosition,

   FunctionCategory category,

   short group,

   short id

)


#### Parameters

*functionTemplatePosition*
:   Template position which is being changed

*category*
:   Function definition category

*group*
:   Function definition group id

*id*
:   Function definition id

Remarks

The method can change type of a function templates when switching function category.
