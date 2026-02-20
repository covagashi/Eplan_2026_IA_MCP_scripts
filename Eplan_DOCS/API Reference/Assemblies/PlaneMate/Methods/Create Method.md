# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaneMate~Create.html

---

Create a PlaneMate.

Syntax

**C#**



public void Create( 

   string strName,

   string strMatchingMateNames,

   MultiLangString pMLSDescription,

   Matrix3D oPosition,

   double dSizeX,

   double dSizeY

)

public:

void Create( 

   String^ strName,

   String^ strMatchingMateNames,

   MultiLangString^ pMLSDescription,

   Matrix3D oPosition,

   double dSizeX,

   double dSizeY

)


#### Parameters

*strName*
:   Name identifying this mate.

*strMatchingMateNames*
:   Names of mates which can be snapped to this mate.

*pMLSDescription*
:   Description of set to this LineMate.

*oPosition*
:   Position represented by transformation matrix.

*dSizeX*
:   Width of the LineMate.

*dSizeY*
:   Height of the LineMate.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when param is `null` value. Check exception message for more info. |
| [System.ArgumentException](#) | Thrown if `strName` has zero length. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when the PlaneMate has already been created. |

Remarks

Names of mates in `strMatchingMateNames` have to be separated by ';' char. It possible to specify that this mate matches all other mates if parameter `strMatchingMateNames` is null, empty or is equal to '\*'. Value "\*-R" of this parameter means that this mate matches all other mates but without mates from mounting rail (name of such mates is 'R').

Names are not case sensitive and can't contain char: '#'.
