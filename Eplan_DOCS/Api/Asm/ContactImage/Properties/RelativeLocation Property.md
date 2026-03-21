# RelativeLocation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~RelativeLocation.html

---

Gets or sets the location of this object relative to the parent.

Syntax

**C#**



public PointD RelativeLocation {get; set;}

public:

property PointD RelativeLocation {

   PointD get();

   void set (    PointD value);

}


Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when object has not been created yet. |

Remarks

Setting value for RelativeLocation change value of `AutoAlign` to `true`.
