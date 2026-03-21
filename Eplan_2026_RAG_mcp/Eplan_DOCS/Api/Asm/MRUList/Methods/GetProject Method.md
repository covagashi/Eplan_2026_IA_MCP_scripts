# GetProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.MRUList~GetProject.html

---

Gets project name from list.

Syntax

**C#**



public string GetProject( 

   uint nIndex

)

public:

String^ GetProject( 

   uint nIndex

)


#### Parameters

*nIndex*
:   Position on list.

Remarks

Warning: projects opened from API don't write automatically into MRUList. This can be done by calling MRUList.SetProject.
