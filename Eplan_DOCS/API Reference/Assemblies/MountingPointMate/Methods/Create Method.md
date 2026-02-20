# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MountingPointMate~Create.html

---

Creates a mounting point mate.

Syntax

**C#**



public void Create( 

   string strName,

   MultiLangString pMLSDescription,

   Matrix3D matrix

)

public:

void Create( 

   String^ strName,

   MultiLangString^ pMLSDescription,

   Matrix3D matrix

)


#### Parameters

*strName*


*pMLSDescription*
:   Description of a mounting point

*matrix*
:   Position represented by transformation matrix.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a param is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when a mate has already been created. |
