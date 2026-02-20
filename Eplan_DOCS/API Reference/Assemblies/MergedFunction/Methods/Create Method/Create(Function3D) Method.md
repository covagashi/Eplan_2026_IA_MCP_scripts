# Create(Function3D) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~Create(Function3D).html

---

Initializes the merged function to cover the function 3D passed as parameter and all the other 'mergable' functions from the device that the input function 3D belongs to. 'Mergable' in this context means, generally, representing the same functional part of the device.

Syntax

**C#**



public void Create( 

   Function3D pFunction3D

)

public:

void Create( 

   Function3D^ pFunction3D

)


#### Parameters

*pFunction3D*
:   Function 3D object from which merged function will be created.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the function 3D is not valid. |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when the function 3D can not be merged. |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the merged function has already been created. |

Remarks

Functions with empty names are unmergable. Only functions with specific placement types can be merged. Placement types of mergable functions are returned by DocumentTypeManager.GetFctDocTypesToMerge() method.
