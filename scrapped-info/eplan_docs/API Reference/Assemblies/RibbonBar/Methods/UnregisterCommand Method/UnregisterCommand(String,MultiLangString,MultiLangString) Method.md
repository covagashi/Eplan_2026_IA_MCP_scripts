# UnregisterCommand(String,MultiLangString,MultiLangString) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.RibbonBar~UnregisterCommand(String,MultiLangString,MultiLangString).html

---

Removes a command from the ribbon. If the ribbon doesn't exist yet, the command will be removed after the system start is finished

Syntax

**C#**



public void UnregisterCommand( 

   string strActionCommandLine,

   MultiLangString multiLangTabName,

   MultiLangString multiLangCommandGroupName

)

public:

void UnregisterCommand( 

   String^ strActionCommandLine,

   MultiLangString^ multiLangTabName,

   MultiLangString^ multiLangCommandGroupName

)


#### Parameters

*strActionCommandLine*
:   Object which are used as a template for a new ribbon command

*multiLangTabName*
:   The name of the tab

*multiLangCommandGroupName*
:   The name of the command group

Remarks

If multiLangTabName or multiLangCommandGroupName is null, the command is removed from the command group Extensions->API
