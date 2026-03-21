# FUNC_ARTICLE_RATED_CURRENT_CONSUMPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic582.html

---

Nominal current consumption # 26505.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_CURRENT_CONSUMPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_CURRENT_CONSUMPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Current that an electrical device or a component absorbs during normal operation.
