# Create(ViewPart,AnyPropertyId) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.ContextPropertyPlacement3D~Create(ViewPart,AnyPropertyId).html

---

Creates the ContextPropertyPlacement3D object.

Syntax

**C#**



public void Create( 

   ViewPart objSource,

   AnyPropertyId idOfProperty

)

public:

void Create( 

   ViewPart^ objSource,

   AnyPropertyId^ idOfProperty

)


#### Parameters

*objSource*
:   [Eplan.EplApi.DataModel.ViewPart](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart.html) object that property value will be displayed.

*idOfProperty*
:   [Eplan.EplApi.DataModel.AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) identifier of property to display.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `oParent` or `oAnyPropertyId` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the ContextPropertyPlacement3D cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the ContextPropertyPlacement3D has already been created. |

Remarks

Method sets value of `parent`s property UseLocalPropertyPlacements to true if it's set to false.
