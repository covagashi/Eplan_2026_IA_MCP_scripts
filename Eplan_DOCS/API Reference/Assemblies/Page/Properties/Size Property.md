# Size Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Size.html

---

Returns the exact size of the page, takes into account page scale. The size is calculated from center of border lines.

Syntax

**C#**



public PointD Size {get;}

public:

property PointD Size {

   PointD get();

}


#### Property Value

Size of a page which is calculated from center of border lines.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when a page has no frame. |
