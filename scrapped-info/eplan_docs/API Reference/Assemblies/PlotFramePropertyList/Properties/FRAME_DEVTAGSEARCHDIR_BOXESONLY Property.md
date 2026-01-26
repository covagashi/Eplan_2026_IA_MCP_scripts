# FRAME_DEVTAGSEARCHDIR_BOXESONLY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_DEVTAGSEARCHDIR_BOXESONLY().html

---

DT adoption: Only from boxes # 12105.

Syntax

**C#**



public PropertyValue FRAME_DEVTAGSEARCHDIR_BOXESONLY {get; set;}

public:

property PropertyValue^ FRAME_DEVTAGSEARCHDIR_BOXESONLY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This plot frame property allows the search direction for DT adoption to be changed. If this property is activated, the DT is only adopted from the box surrounding the function (black box, PLC box) on the corresponding project pages. If the function is not located in a box, no DT can be adopted.
