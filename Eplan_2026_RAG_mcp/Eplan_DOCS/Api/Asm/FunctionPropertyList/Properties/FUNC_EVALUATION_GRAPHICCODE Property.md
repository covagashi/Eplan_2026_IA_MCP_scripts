# FUNC_EVALUATION_GRAPHICCODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_EVALUATION_GRAPHICCODE(Int32).html

---

Graphical display in reports # 20089.

Syntax

**C#**



public PropertyValue FUNC_EVALUATION_GRAPHICCODE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_EVALUATION_GRAPHICCODE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

A max. of 10 additional graphical identifiers for reports that are needed for EPLAN 21 data imports.
