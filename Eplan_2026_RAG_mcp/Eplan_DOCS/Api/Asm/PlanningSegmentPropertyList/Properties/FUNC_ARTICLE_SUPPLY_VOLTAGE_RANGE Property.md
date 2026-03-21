# FUNC_ARTICLE_SUPPLY_VOLTAGE_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1040.html

---

Suppress in bill of materials (if filtered) # 20105.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SUPPRESSINPARTSLIST( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUPPRESSINPARTSLIST {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

This setting allows suppressing the part reference in the bill of materials by specifying an appropriate filter there. A max. of 50 parts references are reported.
