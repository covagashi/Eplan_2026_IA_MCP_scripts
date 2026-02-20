# AddCommand(MultiLangString,String,RibbonIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~AddCommand(MultiLangString,String,RibbonIcon).html

---

Adds command to the ribbon

Syntax

**C#**



public RibbonCommand AddCommand( 

   MultiLangString multiLangButtonText,

   string strActionCommandLine,

   RibbonIcon icon

)

public:

RibbonCommand^ AddCommand( 

   MultiLangString^ multiLangButtonText,

   String^ strActionCommandLine,

   RibbonIcon^ icon

)


#### Parameters

*multiLangButtonText*
:   Command text, multilanguage

*strActionCommandLine*
:   Command line

*icon*
:   Ribbon icon object which is used to create icon based on it

Remarks

The command is added to the command group Extensions->API
