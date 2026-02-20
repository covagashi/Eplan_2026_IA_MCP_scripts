# ReorganizeLegendNumbers Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MountingPanelService~ReorganizeLegendNumbers.html

---

Reorganize legend Ids of a panel layout.

Syntax

**C#**



public void ReorganizeLegendNumbers( 

   Function oMountingPanel,

   long nStartValue,

   long nStepValue,

   MountingPanelService.NumberingDirection nNumberingDirection

)

public:

void ReorganizeLegendNumbers( 

   Function^ oMountingPanel,

   int64 nStartValue,

   int64 nStepValue,

   MountingPanelService.NumberingDirection nNumberingDirection

)


#### Parameters

*oMountingPanel*
:   Mounting panel whose legend numbers will be reorganized.

*nStartValue*
:   Start value for the numbering.

*nStepValue*
:   Step value for the numbering.

*nNumberingDirection*
:   Numbering direction. Allowed values are defined in the enum NUMBERING\_DIRECTION.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown when required parameter is null. |
| **ArgumentException** | Invalid parameter. |
| **ApplicationException** | Needed internal interface could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Error occurred while reorganizing legend numbers. |
