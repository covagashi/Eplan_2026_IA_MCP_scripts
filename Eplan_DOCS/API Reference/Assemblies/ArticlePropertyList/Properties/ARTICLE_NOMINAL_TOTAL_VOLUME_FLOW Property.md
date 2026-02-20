# ARTICLE_NOMINAL_TOTAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_NOMINAL_TOTAL_VOLUME_FLOW().html

---

Nominal total flow rate # 26129.

Syntax

**C#**



public PropertyValue ARTICLE_NOMINAL_TOTAL_VOLUME_FLOW {get; set;}

public:

property PropertyValue^ ARTICLE_NOMINAL_TOTAL_VOLUME_FLOW {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum flow rate that can flow through a system or component under normal operating conditions for the total temperature, total pressure, and gas composition (e.g., humidity) per time unit. This value is usually specified in cubic meters per hour (m³ /h) or liters per minute (l/min).
