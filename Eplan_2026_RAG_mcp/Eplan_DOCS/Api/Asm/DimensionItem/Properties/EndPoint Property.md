# EndPoint Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~EndPoint.html

---

Gets or sets the end point of the DimensionItem.

Syntax

**C#**



public PointD EndPoint {get; set;}

public:

property PointD EndPoint {

   PointD get();

   void set (    PointD value);

}


Remarks

In case of a linear DimensionItem, this specifies the actual location of the dimension line. When setting this property in that case, only one of the point's coordinates is changed (X for vertical and Y for horizontal dimension lines).
