# RegisterCommand(RibbonCommandInfo,RibbonIcon,MultiLangString,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1302.html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   MultiLangString multiLangButtonText,

   string strActionCommandLine,

   MultiLangString multiLangTooltip,

   MultiLangString multiLangDescription,

   RibbonIcon icon

)

public:

RibbonCommand^ AddCommand( 

   MultiLangString^ multiLangButtonText,

   String^ strActionCommandLine,

   MultiLangString^ multiLangTooltip,

   MultiLangString^ multiLangDescription,

   RibbonIcon^ icon

)


#### Parameters

*multiLangButtonText*
:   Text that is set at a button, multilanguage

*strActionCommandLine*
:   Command line of the action

*multiLangTooltip*
:   Tooltip to the command, multilanguage

*multiLangDescription*
:   Description of the command, multilanguage

*icon*
:   Ribbon icon object which are used to create icon based on it

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
