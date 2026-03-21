# DeleteAutoCable(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~DeleteAutoCable(String).html

---

removes automatically created cables and connection definition points. Automatically set names also will be deleted.

Syntax

**C#**



public void DeleteAutoCable( 

   string strFullLinkFileName

)

public:

void DeleteAutoCable( 

   String^ strFullLinkFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project in which the cables will be removed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | invalid parameter. |
| **ApplicationException** | \Internal interface necessary for deleted cables could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when deleting cables please read the exception message. |
