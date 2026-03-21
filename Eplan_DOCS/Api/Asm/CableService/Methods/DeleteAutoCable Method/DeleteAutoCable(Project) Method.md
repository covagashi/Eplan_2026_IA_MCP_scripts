# DeleteAutoCable(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.CableService~DeleteAutoCable(Project).html

---

removes automatically created cables and connection definition points. Automatically set names also will be deleted.

Syntax

**C#**



public void DeleteAutoCable( 

   Project oProject

)

public:

void DeleteAutoCable( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project in which the cables will be removed.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | invalid parameter. |
| **ApplicationException** | \Internal interface necessary for deleted cables could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred when deleting cables please read the exception message. |
