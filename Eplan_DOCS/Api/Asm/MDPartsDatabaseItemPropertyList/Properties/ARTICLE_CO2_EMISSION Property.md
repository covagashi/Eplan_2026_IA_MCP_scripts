# ARTICLE_CO2_EMISSION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CO2_EMISSION().html

---

CO2 emission # 26245.

Syntax

**C#**



public MDPropertyValue ARTICLE_CO2_EMISSION {get; set;}

public:

property MDPropertyValue^ ARTICLE_CO2_EMISSION {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specification of carbon dioxide emission in milligrams per kilowatt-hour. The emission data for air emissions are specified in the unit E3 kg/TJ. They can be converted into the more common unit g/kWh by multiplying by the factor 3.6.
