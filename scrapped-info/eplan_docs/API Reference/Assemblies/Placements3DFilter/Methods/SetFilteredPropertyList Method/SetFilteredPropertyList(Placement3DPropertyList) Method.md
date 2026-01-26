# SetFilteredPropertyList(Placement3DPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placements3DFilter~SetFilteredPropertyList(Placement3DPropertyList).html

---

Sets the [Eplan.EplApi.DataModel.E3D.Placement3DPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList.html) that will be used for searching [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html).

Syntax

**C#**



public void SetFilteredPropertyList( 

   Placement3DPropertyList searchedPropList

)

public:

void SetFilteredPropertyList( 

   Placement3DPropertyList^ searchedPropList

)


#### Parameters

*searchedPropList*
:   List of the P8 properties that will be used for searching [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html). Cannot be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `null` is given as a parameter. |
