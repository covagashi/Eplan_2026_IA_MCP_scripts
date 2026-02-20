# SnapPosition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~SnapPosition.html

---

Position found snap point near mouse position.

Syntax

**C#**



public virtual PointD3D SnapPosition {get; set;}

public:

virtual property PointD3D SnapPosition {

   PointD3D get();

   void set (    PointD3D value);

}


Remarks

This function does not consider ortho-mode or mates.
