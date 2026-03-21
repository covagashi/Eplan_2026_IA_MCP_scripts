# SetPages Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Guiu~Eplan.EplApi.Gui.MRUList~SetPages.html

---

Sets page names.

Syntax

**C#**



public bool SetPages( 

   string strFullLinkFileName,

   string[] lPages

)

public:

bool SetPages( 

   String^ strFullLinkFileName,

   array<String^>^ lPages

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*lPages*
:   Table with page names.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if null was passed as an argument. |
