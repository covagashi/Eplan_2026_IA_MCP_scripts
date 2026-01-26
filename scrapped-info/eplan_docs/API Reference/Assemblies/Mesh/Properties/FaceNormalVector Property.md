# FaceNormalVector Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mesh~FaceNormalVector.html

---

Returns normal vector for face with a given id.

Syntax

**C#**



public ValueType FaceNormalVector( 

   uint id

) {get;}

public:

property ValueType^ FaceNormalVector {

   ValueType^ get(uint id);

}


#### Parameters

*id*
:   Face identifier. Valid values are from 0 to FaceCount-1.

#### Property Value

Normal vector for face with a given id.
