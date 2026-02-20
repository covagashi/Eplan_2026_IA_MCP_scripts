# Remove Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Remove.html

---

Removes the Mate object.

Syntax

**C#**



public virtual void Remove()

public:

virtual void Remove();


Exceptions

| Exception | Description |
| --- | --- |
| [System.InvalidOperationException](#) | Thrown when object can't be removed. |

Remarks

Mate can be removed only when is not read only.

Example

The following code removes a user defined mate.

**C#**

```
//prepare transformation of mate

Matrix3D oTransformation = new Matrix3D();

oTransformation.OffsetX = 20.0;

oTransformation.OffsetY = 20.0;

oTransformation.OffsetZ = 0.0;

//prepare description of mate

Eplan.EplApi.Base.MultiLangString oDescription = new Eplan.EplApi.Base.MultiLangString();

oDescription.AddString(ISOCode.Language.L_en_US, "User defined mounting point number 001.");

//create new point mate object

MountingPointMate oMountingPointMate = new MountingPointMate();

oMountingPointMate.Create("UserMate001", oDescription, oTransformation);

//assign mate to 3D placement

oMP.AddMatePersistent(oMountingPointMate);

//find the new mate

Mate oUserMate001 = oMP.FindTargetMate("UserMate001", false);

//remove the mate

oUserMate001.Remove();

//oPlane.FindTargetMate("UserMate001", false) == null

```
