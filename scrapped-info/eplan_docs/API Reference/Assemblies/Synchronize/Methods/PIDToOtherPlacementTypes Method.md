# PIDToOtherPlacementTypes Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PIDToOtherPlacementTypes.html

---

Synchronization from PID data onto other representations. Corresponds to the Tools' -> 'Synchronization' -> 'PI diagram --> all representation types' ribbon item.

Syntax

**C#**



public void PIDToOtherPlacementTypes( 

   Project oProject

)

public:

void PIDToOtherPlacementTypes( 

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
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. This exception is also thrown when the project doesn't contain any functions to update from. |
