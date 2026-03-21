# OpenPageWithName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~OpenPageWithName.html

---

Opens the page with the name passed to strPageName.

Syntax

**C#**



public Page OpenPageWithName( 

   string strFullLinkFileName,

   string strPageName

)

public:

Page^ OpenPageWithName( 

   String^ strFullLinkFileName,

   String^ strPageName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project.

*strPageName*
:   Name of the page to open.

#### Return Value

The opened Page object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Is thrown in case of invalid parameters. |
| [System.ApplicationException](#) | The graphics editor interface could not be created. |
