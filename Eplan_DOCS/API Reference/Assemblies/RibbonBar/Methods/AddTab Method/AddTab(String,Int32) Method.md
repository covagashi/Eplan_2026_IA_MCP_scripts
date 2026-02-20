# AddTab(String,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddTab(String,Int32).html

---

Adds a new tab to the ribbon

Syntax

**C#**



public RibbonTab AddTab( 

   string strTabName,

   int position

)

public:

RibbonTab^ AddTab( 

   String^ strTabName,

   int position

)


#### Parameters

*strTabName*
:   Name of a new tab

*position*
:   Position of a new tab (0-based)

#### Return Value

Created tab, or null if nothing was created
