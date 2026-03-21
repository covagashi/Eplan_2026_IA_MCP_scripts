# AddIcon Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddIcon.html

---

Adds new icon to the ribbon bar

Syntax

**C#**



public RibbonIcon AddIcon( 

   string svgSource

)

public:

RibbonIcon^ AddIcon( 

   String^ svgSource

)


#### Parameters

*svgSource*
:   Content of svg icon or path to the svg icon file

#### Return Value

Created icon, or null if nothing was created

Remarks

If the icon was added before, ribbon icon will be returned reusing this previous added icon
