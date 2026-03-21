# NumberPCTLoops(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PrePlanningService~NumberPCTLoops(Project).html

---

Numbers all PCTLoops in a Project

Syntax

**C#**



public void NumberPCTLoops( 

   Project pProject

)

public:

void NumberPCTLoops( 

   Project^ pProject

)


#### Parameters

*pProject*
:   Project in which PCTLoops will be numbered. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter `pProject` is a `null` value. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If an Error occurred while numbering PCTLoops. |
