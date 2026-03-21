# FUNC_ARTICLE_EXTERNAL_PLACEMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_EXTERNAL_PLACEMENT(Int32).html

---

External placement # 20917.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_EXTERNAL_PLACEMENT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_EXTERNAL_PLACEMENT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Identifies the part as being externally placed and thus excludes it from panel layout reports. A max. of 50 definitions can be defined using the index.
