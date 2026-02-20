# CablingToAllConnectionTypes Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~CablingToAllConnectionTypes.html

---

Synchronization from 'cabling' connection data onto all other connection types (multi-line, panellayout 3D, single-line)

Syntax

**C#**



public void CablingToAllConnectionTypes( 

   Project oProject

)

public:

void CablingToAllConnectionTypes( 

   Project^ oProject

)


#### Parameters

*oProject*
:   Project that will be synchronized.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |
