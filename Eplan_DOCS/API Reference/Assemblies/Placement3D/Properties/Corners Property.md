# Corners Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Corners.html

---

Represents coordinates of corners

Syntax

**C#**



public Placement3D.CornersClass Corners {get;}

public:

property Placement3D.CornersClass^ Corners {

   Placement3D.CornersClass^ get();

}


Remarks

Property represents corners' coordinates of a Placement3D regarding local coordinate system. They indicate the same part of object 3d, independently of a transformation and a viewpoint. They could be returned as relative or absolute. Following standard of sides is assumed : Front: side with the lowest Y Back : side with highest Y Right : side with highest X Left : side with lowest X Top : side with highest Z Bottom : side with lowest Z The property does not consider any child objects that may stick out of the scope of a Placement3D
