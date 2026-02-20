# BasePoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.ContextPropertyPlacement3D~BasePoint.html

---

Returns [Eplan.EplApi.DataModel.ContextPropertyPlacement.Enums.BasePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement+Enums+BasePoint.html).

Syntax

**C#**



public override ContextPropertyPlacement.Enums.BasePoint BasePoint {set;}

public:

property ContextPropertyPlacement.Enums.BasePoint BasePoint {

   void set (    ContextPropertyPlacement.Enums.BasePoint value) override;

}


#### Property Value

[Eplan.EplApi.DataModel.ContextPropertyPlacement.Enums.BasePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement+Enums+BasePoint.html).

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when cannot set BasePoint by given value. |
| [System.NotImplementedException](#) | Thrown when BasePoint is not implemented. For example for ContextPropertyPlacement placed on page. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |
