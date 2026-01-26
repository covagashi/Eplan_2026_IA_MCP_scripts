# AddFunctionTemplatePosition(MDFunctionTemplatePosition) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPart~AddFunctionTemplatePosition(MDFunctionTemplatePosition).html

---

Adds a copy of FunctionTemplate to the part.

Syntax

**C#**



public MDFunctionTemplatePosition AddFunctionTemplatePosition( 

   MDFunctionTemplatePosition pExistingTemplate

)

public:

MDFunctionTemplatePosition^ AddFunctionTemplatePosition( 

   MDFunctionTemplatePosition^ pExistingTemplate

)


#### Parameters

*pExistingTemplate*
:   Existing function template which will be copied or `null`.

Remarks

Method copies existing function template and adds it at the end of templates list. If parameter is `null` then empty function template is being added.
