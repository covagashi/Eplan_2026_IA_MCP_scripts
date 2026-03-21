# GetMainPlacement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~GetMainPlacement.html

---

Returns main placement this MergedFunction by parameters.

Syntax

**C#**



public void GetMainPlacement( 

   ref Page rPage,

   ref PointD pnt

)

public:

void GetMainPlacement( 

   Page^% rPage,

   PointD% pnt

)


#### Parameters

*rPage*
:   reference to [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) the main placement is placed on

*pnt*
:   reference to [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) holding the coordinates, where the main placement is placed on

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |
