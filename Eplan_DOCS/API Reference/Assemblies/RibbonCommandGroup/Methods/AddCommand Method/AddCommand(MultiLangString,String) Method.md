# AddCommand(MultiLangString,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonCommandGroup~AddCommand(MultiLangString,String).html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   MultiLangString multiLangButtonText,

   string strActionCommandLine

)

public:

RibbonCommand^ AddCommand( 

   MultiLangString^ multiLangButtonText,

   String^ strActionCommandLine

)


#### Parameters

*multiLangButtonText*
:   Text that is set at a button, multilanguage

*strActionCommandLine*
:   Command line of the action

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
