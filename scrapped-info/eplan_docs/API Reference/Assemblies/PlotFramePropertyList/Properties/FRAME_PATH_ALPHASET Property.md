# FRAME_PATH_ALPHASET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.PlotFramePropertyList~FRAME_PATH_ALPHASET(Int32).html

---

String for column designation # 12027.

Syntax

**C#**



public PropertyValue FRAME_PATH_ALPHASET( 

   int index

) {get; set;}

public:

property PropertyValue^ FRAME_PATH_ALPHASET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Set of character strings that overwrite the predefined column designations. Required for the project-wide numbering of columns and entered during automatic numbering. A character string is saved for each index value; max. 1,000 character strings allowed.
