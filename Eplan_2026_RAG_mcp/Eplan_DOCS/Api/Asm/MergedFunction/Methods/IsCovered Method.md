# IsCovered Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~IsCovered.html

---

Returns if the objects is a function or a connection covered by this merged function.

Syntax

**C#**



public bool IsCovered( 

   StorableObject obj

)

public:

bool IsCovered( 

   StorableObject^ obj

)


#### Parameters

*obj*
:   Object that is to be tested.

#### Return Value

true : object is covered by this merged function

false : object is not covered by this merged function

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |
