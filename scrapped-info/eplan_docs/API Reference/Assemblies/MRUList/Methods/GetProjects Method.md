# GetProjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.MRUList~GetProjects.html

---

Gets all project names from list.

Syntax

**C#**



public string[] GetProjects()

public:

array<String^>^ GetProjects();


Remarks

Warning: projects opened from API don't write automatically into MRUList. This can be done by calling MRUList.SetProject.
