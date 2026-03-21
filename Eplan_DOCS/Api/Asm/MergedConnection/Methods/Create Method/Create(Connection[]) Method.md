# Create(Connection[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedConnection~Create(Connection[]).html

---

Initializes the MergedConnection object to cover the connections passed in the array parameter. If the connections cannot be merged together into one merged connection an exception is thrown. connections, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same connectional part of the device.

Syntax

**C#**



public void Create( 

   Connection[] connections

)

public:

void Create( 

   array<Connection^>^ connections

)


#### Parameters

*connections*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `connections` is `null`, emty. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when some connection is not valid. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the connections can not be merged. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the merged connection has already been created. |

Remarks

Only complete connections with specific placement types can be merged. Placement types of mergable connections are returned by DocumentTypeManager.GetFctDocTypesToMergeConnection() method
