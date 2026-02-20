# PanelLayout3DToAllConnectionTypes Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PanelLayout3DToAllConnectionTypes.html

---

Synchronization from 'panellayout 3D' connection data onto all other connection types (multi-line, cabling, single-line)

Syntax

**C#**



public void PanelLayout3DToAllConnectionTypes( 

   Project oProject

)

public:

void PanelLayout3DToAllConnectionTypes( 

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
