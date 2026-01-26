# Page(Page,String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Search~Page(Page,String,String).html

---

Searches on the specified page for a search string. The search settings will influence the result. The found object will be written to the active list of results.

Syntax

**C#**



public void Page( 

   Page pPage,

   string searchString,

   string strFilterScheme

)

public:

void Page( 

   Page^ pPage,

   String^ searchString,

   String^ strFilterScheme

)


#### Parameters

*pPage*
:   Page for which the search is conducted.

*searchString*
:   Text to search for.

*strFilterScheme*
:   Filter scheme. When `null` is passed no filter scheme is used.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the page is not valid. |
| **ApplicationException** | \Internal interface for search could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The search finished with errors. |
