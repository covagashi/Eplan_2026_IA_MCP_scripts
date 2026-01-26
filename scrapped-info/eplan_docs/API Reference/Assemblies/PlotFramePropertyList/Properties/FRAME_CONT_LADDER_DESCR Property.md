# FRAME_CONT_LADDER_DESCR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_CONT_LADDER_DESCR().html

---

Continuous row / column designation # 12031.

Syntax

**C#**



public PropertyValue FRAME_CONT_LADDER_DESCR {get; set;}

public:

property PropertyValue^ FRAME_CONT_LADDER_DESCR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

For ladder logic: The rows are incremented exactly like the columns, that is, each row designation only exists once per page.
