# ARTICLE_PRESSURE_STAGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRESSURE_STAGE().html

---

Pressure level # 26259.

Syntax

**C#**



public PropertyValue ARTICLE_PRESSURE_STAGE {get; set;}

public:

property PropertyValue^ ARTICLE_PRESSURE_STAGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum pressure load that an item or material can withstand without being damaged. This specification is important for components that are operated in pressure systems or under high pressure, such as pipes, valves or pressure vessels. The pressure level is usually expressed in bar or pascal (Pa).
