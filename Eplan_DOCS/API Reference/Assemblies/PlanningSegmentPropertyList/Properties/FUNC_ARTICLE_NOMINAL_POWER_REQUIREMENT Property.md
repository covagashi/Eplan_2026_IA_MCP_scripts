# FUNC_ARTICLE_NOMINAL_POWER_REQUIREMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic961.html

---

Nominal pressure # 26471.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum permissible pressure that an item or piping can withstand under normal operating conditions. This pressure is specified in bar.
