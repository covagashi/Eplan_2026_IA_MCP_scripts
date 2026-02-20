# FUNC_ARTICLE_NOMINAL_WIDTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.PlanningSegmentPropertyList~FUNC_ARTICLE_NOMINAL_WIDTH(Int32).html

---

Nominal size / diameter # 26513.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_WIDTH( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_WIDTH {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Standardized size of connection points and connections in piping systems. The nominal size is a numerical designation for the approximate diameter of the items in a piping system and is often abbreviated as DN (diameter nominal). The nominal size is specified in millimeters and encompasses standardized sizes such as DN 10, DN 20, DN 50, etc.
