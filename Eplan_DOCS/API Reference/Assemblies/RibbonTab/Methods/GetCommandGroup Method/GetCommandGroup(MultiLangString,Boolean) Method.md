# GetCommandGroup(MultiLangString,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonTab~GetCommandGroup(MultiLangString,Boolean).html

---

Gets command group by its name

Syntax

**C#**



public RibbonCommandGroup GetCommandGroup( 

   MultiLangString multiLangName,

   bool checkAnyLanguage

)

public:

RibbonCommandGroup^ GetCommandGroup( 

   MultiLangString^ multiLangName,

   bool checkAnyLanguage

)


#### Parameters

*multiLangName*
:   Name of a command group, multilanguage

*checkAnyLanguage*
:   Check if command group exist in any (not only current) language

Remarks

When the command group was previously added in different language than current, then using MultiLangString with group name in various languages can be helpful to find such command group.
