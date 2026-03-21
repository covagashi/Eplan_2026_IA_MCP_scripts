# SelectedProjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~SelectedProjects.html

---

Return the selected projects of the active dialog as an array. If you select elements from different projects inside of one dialog you can determinate the selected projects.

Syntax

**C#**



public Project[] SelectedProjects {get;}

public:

property array<Project^>^ SelectedProjects {

   array<Project^>^ get();

}


#### Property Value

Returns all selected Projects of the active dialog.
