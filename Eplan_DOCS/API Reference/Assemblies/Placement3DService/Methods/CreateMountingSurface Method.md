# CreateMountingSurface Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Placement3DService~CreateMountingSurface.html

---

Creates mounting surface for the face identified by points and normal vector.

Syntax

**C#**



public Plane CreateMountingSurface( 

   Function3D pFunction3D,

   PointD3D[] oFacePoints,

   Vector3D oDirection,

   bool bCombineSurfaces

)

public:

Plane^ CreateMountingSurface( 

   Function3D^ pFunction3D,

   array<PointD3D>^ oFacePoints,

   Vector3D oDirection,

   bool bCombineSurfaces

)


#### Parameters

*pFunction3D*
:   3D function for which mounting surface will be created. Cannot be `null`.

*oFacePoints*
:   Points of face of Function3D mesh.

*oDirection*
:   Normal vector for face of Function3D mesh.

*bCombineSurfaces*
:   Combines coplanar surfaces when true.

#### Return Value

Mounting surface.

Example

Example shows how to create new mounting surface based on position of given mates.

**C#**

```
Plane CreateMountingSurfaceForGivenBasePoints(Function3D oFunc3D, string oMateName1, string oMateName2, string oMateName3)

{

    Mate[] arrMates1 = oFunc3D.GetTargetMates(true);

    Mate oMate1 = oFunc3D.FindTargetMate(oMateName1, false);

    Mate oMate2 = oFunc3D.FindTargetMate(oMateName2, false);

    Mate oMate3 = oFunc3D.FindTargetMate(oMateName3, false);

    Matrix3D oAbsTransfInv = oFunc3D.AbsoluteTransformation;

    oAbsTransfInv.Invert();

    PointD3D oPos1 = GetRelativePointD3D(oAbsTransfInv, oMate1.Transformation);

    PointD3D oPos2 = GetRelativePointD3D(oAbsTransfInv, oMate2.Transformation);

    PointD3D oPos3 = GetRelativePointD3D(oAbsTransfInv, oMate3.Transformation);

    Mesh oMesh = oFunc3D.Mesh;

    PointD3D[] arrFoundFace = null;

    Vector3D oNormalVector = new Vector3D();

    for (uint i = 1; i < oMesh.FaceCount; i++)

    {

        try

        {

            PointD3D[] arrFace = oMesh.get_FacePoints(i);

            oNormalVector = (Vector3D)oMesh.get_FaceNormalVector(i);

            if (IsPointInFaceBorder(arrFace, oPos1) &&

                IsPointInFaceBorder(arrFace, oPos2) &&

                    IsPointInFaceBorder(arrFace, oPos3))

            {

                arrFoundFace = arrFace;

                break;

            }

        }

        catch

        {

        }

    }

    if (arrFoundFace != null && arrFoundFace.Length > 0)

    {

        Plane oMountingSurface = new Placement3DService().CreateMountingSurface(oFunc3D, arrFoundFace, oNormalVector, true);

        return oMountingSurface;

    }

    return null;

}

PointD3D GetRelativePointD3D(Matrix3D oAbsTrasfInv, Matrix3D oPointTransf)

{

    Point3D oRelativePoint = oAbsTrasfInv.Transform(oPointTransf.Transform(new Point3D(0, 0, 0)));

    return new PointD3D(oRelativePoint.X, oRelativePoint.Y, oRelativePoint.Z);

}

bool IsPointInFaceBorder(PointD3D[] arrFace, PointD3D oPoint)

{

    foreach (PointD3D oFacePoint in arrFace)

    {

        if ((Math.Abs(oFacePoint.X - oPoint.X) < 1) && (Math.Abs(oFacePoint.Y - oPoint.Y) < 1) && (Math.Abs(oFacePoint.Z - oPoint.Z) < 1))

            return true;

    }

    return false;

}

```
