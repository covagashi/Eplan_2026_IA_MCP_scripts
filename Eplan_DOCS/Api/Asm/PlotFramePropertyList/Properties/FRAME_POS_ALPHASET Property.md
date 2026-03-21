# FRAME_POS_ALPHASET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_POS_ALPHASET(Int32).html

---

String for row designation # 12028.

Syntax

**C#**



public PropertyValue FRAME_POS_ALPHASET( 

   int index

) {get; set;}

public:

property PropertyValue^ FRAME_POS_ALPHASET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Set of character strings that overwrite the predefined row designations. Required for the project-wide numbering of rows and entered during automatic numbering. A character string is saved for each index value; max. 1,000 character strings allowed.
