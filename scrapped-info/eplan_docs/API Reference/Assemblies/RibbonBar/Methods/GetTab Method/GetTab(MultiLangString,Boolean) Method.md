# GetTab(MultiLangString,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~GetTab(MultiLangString,Boolean).html

---

Returns tab by name, multilanguage

Syntax

**C#**



public RibbonTab GetTab( 

   MultiLangString multiLangTabName,

   bool checkAnyLanguage

)

public:

RibbonTab^ GetTab( 

   MultiLangString^ multiLangTabName,

   bool checkAnyLanguage

)


#### Parameters

*multiLangTabName*
:   Name of a tab, multilanguage

*checkAnyLanguage*
:   Check if tab exist in any (not only current) language

Remarks

When the tab was previously added in different language than current, then using MultiLangString with tab name in various languages can be helpful to find such tab.
