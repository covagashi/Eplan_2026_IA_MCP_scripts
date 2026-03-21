# FRAME_POSITIONSIZE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_POSITIONSIZE(Int32).html

---

Row height # 12002.

Syntax

**C#**



public PropertyValue FRAME_POSITIONSIZE( 

   int index

) {get; set;}

public:

property PropertyValue^ FRAME_POSITIONSIZE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Height of the grid rows.
