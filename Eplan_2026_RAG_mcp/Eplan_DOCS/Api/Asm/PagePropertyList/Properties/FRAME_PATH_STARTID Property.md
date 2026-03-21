# FRAME_PATH_STARTID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~FRAME_PATH_STARTID().html

---

Start value (column) # 12025.

Syntax

**C#**



public PropertyValue FRAME_PATH_STARTID {get; set;}

public:

property PropertyValue^ FRAME_PATH_STARTID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

The column numbers of the grid are normally numbered from left to right (starting with 0). A different starting value can be provided here; this is useful for project-wide numbering.
