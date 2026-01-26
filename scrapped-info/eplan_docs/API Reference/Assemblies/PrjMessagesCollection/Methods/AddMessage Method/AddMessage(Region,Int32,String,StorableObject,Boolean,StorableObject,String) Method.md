# AddMessage(Region,Int32,String,StorableObject,Boolean,StorableObject,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1301.html

---

Adds a command to the ribbon. If the ribbon doesn't exist yet, the command will be added after the system start is finished

Syntax

**C#**



public void RegisterCommand( 

   RibbonCommandInfo ribbonCommandInfo,

   RibbonIcon icon,

   MultiLangString multiLangTabName,

   MultiLangString multiLangCommandGroupName

)

public:

void RegisterCommand( 

   RibbonCommandInfo^ ribbonCommandInfo,

   RibbonIcon^ icon,

   MultiLangString^ multiLangTabName,

   MultiLangString^ multiLangCommandGroupName

)


#### Parameters

*ribbonCommandInfo*
:   Object which are used as a template for a new ribbon command

*icon*
:   Ribbon icon object which are used to create icon based on it

*multiLangTabName*
:   The name of the tab

*multiLangCommandGroupName*
:   The name of the command group

Remarks

If multiLangTabName or multiLangCommandGroupName is null, the command is added to the command group Extensions->API
