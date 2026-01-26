# IsSurfaceFilled Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PolyLine~IsSurfaceFilled.html

---

This property specifies if the polyline is filled. When the polyline is not closed setting this property throws an exception

Syntax

**C#**



public virtual bool IsSurfaceFilled {get; set;}

public:

virtual property bool IsSurfaceFilled {

   bool get();

   void set (    bool value);

}


#### Property Value

true : polyline is filed

false : polyline is not filled
