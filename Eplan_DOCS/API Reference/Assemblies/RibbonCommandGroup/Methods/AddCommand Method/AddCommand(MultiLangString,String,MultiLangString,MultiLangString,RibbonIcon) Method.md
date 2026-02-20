# AddCommand(MultiLangString,String,MultiLangString,MultiLangString,RibbonIcon) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1303.html

---

Adds new command to the command group

Syntax

**C#**



public RibbonCommand AddCommand( 

   MultiLangString multiLangButtonText,

   string strActionCommandLine,

   MultiLangString tooltip,

   MultiLangString description

)

public:

RibbonCommand^ AddCommand( 

   MultiLangString^ multiLangButtonText,

   String^ strActionCommandLine,

   MultiLangString^ tooltip,

   MultiLangString^ description

)


#### Parameters

*multiLangButtonText*
:   Text that is set at a button, multilanguage

*strActionCommandLine*
:   Command line of the action

*tooltip*
:   Tooltip to the command, multilanguage

*description*
:   Description of the command, multilanguage

#### Return Value

Created command, or null if nothing was created

Remarks

The method can add a command only to a custom group.
