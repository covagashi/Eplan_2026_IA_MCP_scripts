# IsCovered Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~IsCovered.html

---

Returns if the objects is a connection covered by this merged connection.

Syntax

**C#**



public bool IsCovered( 

   Connection connection

)

public:

bool IsCovered( 

   Connection^ connection

)


#### Parameters

*connection*
:   Object that is to be tested.

#### Return Value

true : object is covered by this merged connection

false : object is not covered by this merged connection

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |
