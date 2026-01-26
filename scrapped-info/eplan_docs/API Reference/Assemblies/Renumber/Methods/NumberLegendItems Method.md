# NumberLegendItems Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Renumber~NumberLegendItems.html

---

Number legend Ids of a pro panel objects.

Syntax

**C#**



public void NumberLegendItems( 

   InstallationSpace oInstallationSpace,

   long nStartValue,

   long nStepValue,

   Renumber.Enums.NumberingDirection3D nNumberingDirection,

   bool fSameNumbers

)

public:

void NumberLegendItems( 

   InstallationSpace^ oInstallationSpace,

   int64 nStartValue,

   int64 nStepValue,

   Renumber.Enums.NumberingDirection3D nNumberingDirection,

   bool fSameNumbers

)


#### Parameters

*oInstallationSpace*
:   installation space whose legend numbers will be numbered.

*nStartValue*
:   Start value for the numbering.

*nStepValue*
:   Step value for the numbering.

*nNumberingDirection*
:   Numbering direction. Allowed values are defined in the enum NumberingDirection3D.

*fSameNumbers*
:   If true then set same numbers for identical devices. Identical devices have the same partnumber.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown when required parameter is null. |
| **ArgumentException** | Invalid parameter. |
| **ApplicationException** | Needed internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Error occurred while numbering legend ids. |
