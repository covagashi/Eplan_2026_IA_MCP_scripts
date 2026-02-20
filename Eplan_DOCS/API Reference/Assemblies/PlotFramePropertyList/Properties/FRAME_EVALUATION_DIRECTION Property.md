# FRAME_EVALUATION_DIRECTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_EVALUATION_DIRECTION().html

---

Reporting direction # 12103.

Syntax

**C#**



public PropertyValue FRAME_EVALUATION_DIRECTION {get; set;}

public:

property PropertyValue^ FRAME_EVALUATION_DIRECTION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Indicates the reporting direction for a plot frame:

0 = Vertical,

1 = Horizontal.

For projects according to IEC standards, the reporting direction is typically "vertical"; for projects according to the NFPA standards, it is usually horizontal. For projects according to the GOST standard, the reporting direction is typically "vertical"; a column numbered from right to left and a row numbered from the bottom to top can also be set via the properties "Inverse column numbering" (ID 12035) and "Inverse row numbering" (ID 12036).
