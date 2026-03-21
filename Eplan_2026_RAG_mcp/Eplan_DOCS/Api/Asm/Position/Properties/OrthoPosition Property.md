# OrthoPosition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~OrthoPosition.html

---

Cursor position considering ortho-mode.

Syntax

**C#**



public virtual PointD3D OrthoPosition {get; set;}

public:

virtual property PointD3D OrthoPosition {

   PointD3D get();

   void set (    PointD3D value);

}


Remarks

If ortho-mode is off, then this position is the same as SnapPosition does not consider Mates.
