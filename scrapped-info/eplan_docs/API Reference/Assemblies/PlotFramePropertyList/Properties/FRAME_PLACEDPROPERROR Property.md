# FRAME_PLACEDPROPERROR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_PLACEDPROPERROR(Int32).html

---

Error: Property placement # 12101.

Syntax

**C#**



public PropertyValue FRAME_PLACEDPROPERROR( 

   int index

) {get; set;}

public:

property PropertyValue^ FRAME_PLACEDPROPERROR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1024.

Indicates whether a problem occurred with any placed properties during the data transfer of plot frames. Max. of 1,024 are recorded.
