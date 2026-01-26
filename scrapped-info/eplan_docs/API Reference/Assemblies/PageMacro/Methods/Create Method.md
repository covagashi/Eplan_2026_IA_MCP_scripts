# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PageMacro~Create.html

---

Writes a macro file from the pages and then if there was at least one valid page, opens created macro.

Syntax

**C#**



public void Create( 

   string macroFileName,

   Page[] pPages,

   MultiLangString strDescription

)

public:

void Create( 

   String^ macroFileName,

   array<Page^>^ pPages,

   MultiLangString^ strDescription

)


#### Parameters

*macroFileName*
:   The name (inclusive path) for the macro file. Parameter value must include valid extension (otherwise an exception is thrown).

*pPages*
:   The pages the macro should contain

*strDescription*
:   The description for this macro file or null when no description should be set.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameters are not valid |

Remarks

All pages have to be from this same project.
