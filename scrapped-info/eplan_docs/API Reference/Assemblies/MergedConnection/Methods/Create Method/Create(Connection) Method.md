# Create(Connection) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~Create(Connection).html

---

Initializes the merged connection to cover the connection passed as parameter and all the other 'mergable' connections from the input connection belongs to. 'Mergable' in this context means, generally, representing the same corresponding connections with different placement types.

Syntax

**C#**



public void Create( 

   Connection connIn

)

public:

void Create( 

   Connection^ connIn

)


#### Parameters

*connIn*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `connection` is `null`. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the connection is not valid. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the connection can not be merged. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the merged connection has already been created. |

Remarks

Only complete connections with specific placement types can be merged. Placement types of mergable connections are returned by DocumentTypeManager.GetFctDocTypesToMergeConnection() method
