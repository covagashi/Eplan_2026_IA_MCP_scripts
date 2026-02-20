# FUNC_ARTICLE_NOMINAL_VOLUMETRIC_FLOW_OF_COMPRESSED_AIR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic967.html

---

Nominal size / connection size # 26515.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_WIDTH_CONNECTION_SIZE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Nominal specification for the diameter of the process connection point, e.g. DN 25. The nominal size is a numerical size designation that is used for the items for which the outside diameter or thread size is not specified. Describes the size of connection points and connections in piping systems with regard to the connection compatibility of components such as pipes or fittings.
