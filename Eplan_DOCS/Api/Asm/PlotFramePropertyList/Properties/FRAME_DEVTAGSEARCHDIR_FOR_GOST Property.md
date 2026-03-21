# FRAME_DEVTAGSEARCHDIR_FOR_GOST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_DEVTAGSEARCHDIR_FOR_GOST().html

---

DT adoption: Search direction conforming to GOST standard # 12104.

Syntax

**C#**



public PropertyValue FRAME_DEVTAGSEARCHDIR_FOR_GOST {get; set;}

public:

property PropertyValue^ FRAME_DEVTAGSEARCHDIR_FOR_GOST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This plot frame property allows the search direction for DT adoption to be changed to suit the GOST standard. If this property is activated, then in plot frames with a "Vertical" report generation direction, the DT is searched for towards the right and with a "Horizontal" report generation direction the DT is searched for downwards.
