# Create(SymbolReference,AnyPropertyId,RelationType,Int32) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic712.html

---

Creates the PropertyPlacement object related to parent.

Syntax

**C#**



public void Create( 

   SymbolReference pParent,

   AnyPropertyId propId,

   PropertyPlacement.RelationType eRel,

   int iRelIndex

)

public:

void Create( 

   SymbolReference^ pParent,

   AnyPropertyId^ propId,

   PropertyPlacement.RelationType eRel,

   int iRelIndex

)


#### Parameters

*pParent*
:   [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) object that's referenced object property value will be displayed.

*propId*
:   [Eplan.EplApi.DataModel.AnyPropertyId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.AnyPropertyId.html) identifier of property to display.

*eRel*
:   [PropertyPlacement.RelationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement+RelationType.html)Relation type. One of possible relations: Main function article, main function article reference etc.

*iRelIndex*
:   Article reference position of related object.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `parent` is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the PropertyPlacement cannot be created. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the PropertyPlacement has already been created. |

Remarks

Method sets value of object related to `parent`s property UseLocalPropertyPlacements to true if it's set to false and the selected scheme to 'User-defined'.
