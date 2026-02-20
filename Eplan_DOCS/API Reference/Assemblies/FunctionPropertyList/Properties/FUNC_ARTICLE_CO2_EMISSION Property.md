# FUNC_ARTICLE_CO2_EMISSION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_CO2_EMISSION(Int32).html

---

CO2 emission # 26246.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CO2_EMISSION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CO2_EMISSION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specification of carbon dioxide emission in milligrams per kilowatt-hour. The emission data for air emissions are specified in the unit E3 kg/TJ. They can be converted into the more common unit g/kWh by multiplying by the factor 3.6.
