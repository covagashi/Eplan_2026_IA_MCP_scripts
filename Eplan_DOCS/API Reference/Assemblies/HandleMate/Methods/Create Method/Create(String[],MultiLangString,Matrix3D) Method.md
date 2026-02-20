# Create(String[],MultiLangString,Matrix3D) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.HandleMate~Create(String[],MultiLangString,Matrix3D).html

---

Creates a handle with a list of assigned mounting points.

Syntax

**C#**



public void Create( 

   string[] matchingMateNames,

   MultiLangString pMLSDescription,

   Matrix3D matrix

)

public:

void Create( 

   array<String^>^ matchingMateNames,

   MultiLangString^ pMLSDescription,

   Matrix3D matrix

)


#### Parameters

*matchingMateNames*
:   Names of mates which can be snapped to this mate.

*pMLSDescription*
:   Description of the handle

*matrix*
:   Position represented by transformation matrix.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the PointMate has already been created. |
