# FRAME_ROW_DESC_OF_NON_LOGICAL_PAGES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_ROW_DESC_OF_NON_LOGICAL_PAGES().html

---

Show column designation on non-logical pages # 12014.

Syntax

**C#**



public PropertyValue FRAME_ROW_DESC_OF_NON_LOGICAL_PAGES {get; set;}

public:

property PropertyValue^ FRAME_ROW_DESC_OF_NON_LOGICAL_PAGES {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Specifies whether the column designations for this plot frame should also be output on non-logic pages (non-schematic pages). By default, designations are suppressed on non-logical pages.
