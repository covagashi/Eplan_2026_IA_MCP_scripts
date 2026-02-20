# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingLineMate~Create.html

---

Creates a mounting line mate.

Syntax

**C#**



public void Create( 

   string strName,

   MultiLangString pMLSDescription,

   PointD3D pntStart,

   PointD3D pntEnd

)

public:

void Create( 

   String^ strName,

   MultiLangString^ pMLSDescription,

   PointD3D pntStart,

   PointD3D pntEnd

)


#### Parameters

*strName*
:   Name identifying the mate.

*pMLSDescription*
:   Description

*pntStart*
:   Beginning of the line mate, relative.

*pntEnd*
:   End of the line mate, relative.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strName` has zero length. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the LineMate has already been created. |
