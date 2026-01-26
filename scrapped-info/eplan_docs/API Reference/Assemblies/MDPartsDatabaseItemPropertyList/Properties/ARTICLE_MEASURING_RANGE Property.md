# ARTICLE_MEASURING_RANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_MEASURING_RANGE().html

---

Measuring range # 26181.

Syntax

**C#**



public MDPropertyValue ARTICLE_MEASURING_RANGE {get; set;}

public:

property MDPropertyValue^ ARTICLE_MEASURING_RANGE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Range between the smallest and largest value within which a measuring instrument or sensor can carry out precise measurements. Example: In the case of a temperature sensor with a measuring range of -50 °C to +150 °C, the sensor can measure temperatures within this range precisely.
