# FUNC_ARTICLE_RATED_POWER_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_POWER_MIN(Int32).html

---

Nominal power (in kW), min. # 26481.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_POWER_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_POWER_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Suitable minimum possible nominal power in kilowatts (kW).
