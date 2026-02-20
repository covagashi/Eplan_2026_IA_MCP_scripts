# AddFilter Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~AddFilter.html

---

Add a filter which files are shown. When the user selects one filter in the decider dialog, only files of this type are displayed.

Syntax

**C#**



public void AddFilter( 

   string strDescription,

   string strExtension

)

public:

void AddFilter( 

   String^ strDescription,

   String^ strExtension

)


#### Parameters

*strDescription*
:   The description visible to the user, p.e. "Text files \*.txt"

*strExtension*
:   The filter, p.e. "\*.txt"

Remarks

When the strDescription is empty, the system fills it automatically. This is the description used in EPLAN when the same filter is registered there or a automatically formed one from the extensions. The filter also influence the path the file select dialog is opened first. Some of the registered extensions have a standard path. When the standard path is the same for all extensions, this standard path is used. It is possible to set a custom StandardPath with the function CustomDefaultPath.
