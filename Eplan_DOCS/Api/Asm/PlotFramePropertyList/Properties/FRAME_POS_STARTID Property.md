# FRAME_POS_STARTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_POS_STARTID().html

---

Start value (row) # 12026.

Syntax

**C#**



public PropertyValue FRAME_POS_STARTID {get; set;}

public:

property PropertyValue^ FRAME_POS_STARTID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The row numbers of the grid are normally numbered from left to right (starting with 0). A different starting value can be provided here; this is useful for project-wide numbering.
