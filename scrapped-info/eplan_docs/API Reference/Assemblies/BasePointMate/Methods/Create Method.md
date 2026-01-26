# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BasePointMate~Create.html

---

Creates a base point mate.

Syntax

**C#**



public void Create( 

   BasePointMate.Enums.Name nName,

   MultiLangString pMLSDescription,

   Matrix3D matrix

)

public:

void Create( 

   BasePointMate.Enums.Name nName,

   MultiLangString^ pMLSDescription,

   Matrix3D matrix

)


#### Parameters

*nName*
:   Name (enumerated)

*pMLSDescription*
:   Description of a point

*matrix*
:   Position represented by transformation matrix.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when a param is `null`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when a point mate has already been created. |
