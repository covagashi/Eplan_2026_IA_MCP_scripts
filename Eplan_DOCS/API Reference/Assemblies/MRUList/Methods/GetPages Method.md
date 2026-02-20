# GetPages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.MRUList~GetPages.html

---

Gets all page names.

Syntax

**C#**



public string[] GetPages( 

   string strFullLinkFileName

)

public:

array<String^>^ GetPages( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if null was passed as an argument. |
