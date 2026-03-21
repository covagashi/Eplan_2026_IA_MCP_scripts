# MountingSurface Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane~MountingSurface.html

---

Size of mounting surface beginning relatively to the origin of plane. (x == width, y == height)

Syntax

**C#**



public PointD MountingSurface {get; set;}

public:

property PointD MountingSurface {

   PointD get();

   void set (    PointD value);

}


Remarks

The origin and the orientation of the plane are defined in its absolute transformation (AbsoluteTransformation property). Please use RelativeTransformation property to set offsets of a mounting surface.
