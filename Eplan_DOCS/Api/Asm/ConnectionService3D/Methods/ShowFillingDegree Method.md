# ShowFillingDegree Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ConnectionService3D~ShowFillingDegree.html

---

Show or hide filling degree.

Syntax

**C#**



public void ShowFillingDegree( 

   bool bShow

)

public:

void ShowFillingDegree( 

   bool bShow

)


#### Parameters

*bShow*
:   Show filling degree, if bShow==true, otherwise hide filling degree.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when necessary argument is `null`. |
| [System.ApplicationException](#) | An interface used for export could not be created. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the file system. |
