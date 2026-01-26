# Create(Placement3D,AnyPropertyId) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.ContextPropertyPlacement3D~Create(Placement3D,AnyPropertyId).html

---

Creates the ContextPropertyPlacement3D object.

Syntax

**C#**



public void Create( 

   Placement3D objSource,

   AnyPropertyId propId

)

public:

void Create( 

   Placement3D^ objSource,

   AnyPropertyId^ propId

)


#### Parameters

*objSource*
:   [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) object that property value will be displayed.

*propId*
:   [Eplan.EplApi.DataModel.AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) identifier of property to display.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `oParent` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the ContextPropertyPlacement3D cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the ContextPropertyPlacement3D has already been created. |

Remarks

Method sets value of `oParent`s property UseLocalPropertyPlacements to true if it's set to false.
