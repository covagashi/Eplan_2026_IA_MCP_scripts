# ClosePage Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit~ClosePage.html

---

closes a page and the associated GEDs

Syntax

**C#**



public bool ClosePage( 

   Page page

)

public:

bool ClosePage( 

   Page^ page

)


#### Parameters

*page*
:   page to close.

#### Return Value

'¢ TRUE, if everything is alright  
'¢ FALSE otherwise.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of NULL parameters. |
| [System.ArgumentException](#) | Is thrown in case of invalid Page. |
