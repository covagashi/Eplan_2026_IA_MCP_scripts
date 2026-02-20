# FRAME_PATHSIZE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_PATHSIZE(Int32).html

---

Column width # 12102.

Syntax

**C#**



public PropertyValue FRAME_PATHSIZE( 

   int index

) {get; set;}

public:

property PropertyValue^ FRAME_PATHSIZE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Double.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Width of grid columns. A max. of 1,000 is allowed.
