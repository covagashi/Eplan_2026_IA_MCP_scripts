# FunctionDefinition Constructor(Project,FunctionCategory,MultiLangString,MultiLangString)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic210.html

---

Constructs and initializes a FunctionDefinition object with the specified function's category, group and ID. Note: The specified function definition must exist in the project's standard function definitions library

Syntax

**C#**



public FunctionDefinition( 

   Project prj,

   FunctionCategory funcCategory,

   MultiLangString funcGroupName,

   MultiLangString funcDefName

)

public:

FunctionDefinition( 

   Project^ prj,

   FunctionCategory funcCategory,

   MultiLangString^ funcGroupName,

   MultiLangString^ funcDefName

)


#### Parameters

*prj*


*funcCategory*
:   Category of the function definition.

*funcGroupName*
:   Group of the function definition (e.g. "Ader/Draht").

*funcDefName*
:   Identification name of the function definition (e.g. "BrÃ¼cke"). This name for a specific function definition is returned by the FunctionDefinition::Name property.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the specified function definition (category, group and ID) doesn't exists in the project's function definitions library. |

Remarks

Note: Only the first language strings passed by funcGroupName and funcIDName are taken into account.

Example

**C#**

```
MultiLangString grpName = new MultiLangString();

grpName.AddString(ISOCode.Language.L_de_DE, "Ader/Draht");

MultiLangString idName = new MultiLangString();

idName.AddString(ISOCode.Language.L_de_DE, "Brücke");

FunctionDefinition fctDef = new FunctionDefinition(prj, funcCategory, grpName, idName);
```
