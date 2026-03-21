# FUNC_ARTICLE_LIFETIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_LIFETIME(Int32).html

---

Service time # 20909.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_LIFETIME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_LIFETIME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

The time during which a technical system or object can be used without exchanging core components or a complete breakdown. A max. of 50 definitions can be defined using the index.
