# FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC(Int32).html

---

Nominal voltage (AC) # 26491.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_VOLTAGE_FOR_AC {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specified value of the electrical voltage for alternating current.
