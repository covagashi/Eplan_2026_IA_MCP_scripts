# GetCurrentProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~GetCurrentProject.html

---

Determines the active project.

Syntax

**C#**



public Project GetCurrentProject( 

   bool bUseSelDlg

)

public:

Project^ GetCurrentProject( 

   bool bUseSelDlg

)


#### Parameters

*bUseSelDlg*
:   if set to true\: Opens an additional selection dialog, if more than one project was selected in the page browser.

#### Return Value

return != null: the active project return = null: no project is open

Remarks

When 'Cancel' button was pressed in the selection dialog, 1st open project will be returned.
