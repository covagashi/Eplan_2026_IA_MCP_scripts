# FUNC_ARTICLE_SHOCK_LOAD Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_SHOCK_LOAD(Int32).html

---

Shock load # 26585.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SHOCK_LOAD( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SHOCK_LOAD {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Current increase as a multiple of the nominal current due to short-term current peaks or voltage peaks.
