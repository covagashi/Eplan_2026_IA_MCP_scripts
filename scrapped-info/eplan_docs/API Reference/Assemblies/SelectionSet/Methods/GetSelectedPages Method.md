# GetSelectedPages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~GetSelectedPages.html

---

Gets the selected pages.

Syntax

**C#**



public Page[] GetSelectedPages()

public:

array<Page^>^ GetSelectedPages();


#### Return Value

\returns array of selected pages.

Remarks

Returns all selected pages. When a node is selected, all pages inside are returned.
