# CursorPosition Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~CursorPosition.html

---

Position of mouse in the world coordinate system

Syntax

**C#**



public virtual PointD3D CursorPosition {get; set;}

public:

virtual property PointD3D CursorPosition {

   PointD3D get();

   void set (    PointD3D value);

}


Remarks

This function does not consider grid-snap, object-snap ortho-mode or mates.
