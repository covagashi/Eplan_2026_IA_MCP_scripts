# FRAME_ADD_PAGENAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_ADD_PAGENAME().html

---

Add page names # 12030.

Syntax

**C#**



public PropertyValue FRAME_ADD_PAGENAME {get; set;}

public:

property PropertyValue^ FRAME_ADD_PAGENAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, the page name is added to the column designation (page name + column designation). Relevant for the NFPA standard.
