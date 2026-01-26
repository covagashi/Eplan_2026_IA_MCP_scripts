# BasePoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement~BasePoint.html

---

Returns [ContextPropertyPlacement.Enums.BasePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement+Enums+BasePoint.html).

Syntax

**C#**



public virtual ContextPropertyPlacement.Enums.BasePoint BasePoint {get; set;}

public:

virtual property ContextPropertyPlacement.Enums.BasePoint BasePoint {

   ContextPropertyPlacement.Enums.BasePoint get();

   void set (    ContextPropertyPlacement.Enums.BasePoint value);

}


#### Property Value

[ContextPropertyPlacement.Enums.BasePoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ContextPropertyPlacement+Enums+BasePoint.html).

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidArgumentException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidArgumentException.html) | Thrown when cannot set BasePoint by given value. |
| [System.NotImplementedException](#) | Thrown when BasePoint is not implemented. For example for ContextPropertyPlacement placed on page. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal function fails. |
