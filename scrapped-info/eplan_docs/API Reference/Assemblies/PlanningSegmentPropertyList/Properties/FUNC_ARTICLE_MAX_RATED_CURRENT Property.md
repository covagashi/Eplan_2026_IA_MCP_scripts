# FUNC_ARTICLE_MAX_RATED_CURRENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic954.html

---

Nominal power (in kW), max. # 26479.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MAX_RATED_POWER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MAX_RATED_POWER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Suitable maximum possible nominal power in kilowatts (kW).
