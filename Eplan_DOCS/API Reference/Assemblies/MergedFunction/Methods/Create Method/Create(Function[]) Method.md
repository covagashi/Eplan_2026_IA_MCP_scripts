# Create(Function[]) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create(Function[]).html

---

Initializes the MergedFunction object to cover the functions passed in the array parameter. If the functions cannot be merged together into one merged function an exception is thrown. Functions, generally, cannot be merged together if they belong to different devices or they are of different categories. To be merged, they have to represent the same functional part of the device.

Syntax

**C#**



public void Create( 

   Function[] functions

)

public:

void Create( 

   array<Function^>^ functions

)


#### Parameters

*functions*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `functions` is `null`, emty. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when some function is not valid. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the functions can not be merged. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the merged function has already been created. |

Remarks

Functions with empty names are unmergable. Only functions with specific placement types can be merged. Placement types of mergable functions are returned by DocumentTypeManager.GetFctDocTypesToMerge() method
