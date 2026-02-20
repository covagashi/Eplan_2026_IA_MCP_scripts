# Create(SymbolReference,AnyPropertyId) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~Create(SymbolReference,AnyPropertyId).html

---

Creates the PropertyPlacement object.

Syntax

**C#**



public void Create( 

   SymbolReference parent,

   AnyPropertyId propId

)

public:

void Create( 

   SymbolReference^ parent,

   AnyPropertyId^ propId

)


#### Parameters

*parent*
:   [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) object that property value will be displayed.

*propId*
:   [Eplan.EplApi.DataModel.AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) identifier of property to display.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `parent` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the PropertyPlacement cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the PropertyPlacement has already been created. |

Remarks

Method sets value of `parent`s property UseLocalPropertyPlacements to true if it's set to false and the selected scheme to 'User-defined'.
