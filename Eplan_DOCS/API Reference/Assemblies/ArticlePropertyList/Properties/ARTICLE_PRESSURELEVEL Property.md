# ARTICLE_PRESSURELEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PRESSURELEVEL().html

---

Nominal pressure level # 22226.

Syntax

**C#**



public PropertyValue ARTICLE_PRESSURELEVEL {get; set;}

public:

property PropertyValue^ ARTICLE_PRESSURELEVEL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. The nominal pressure of a pipe system specifies a reference value. The designation PN ("Pressure Nominal") is used, followed by a whole number without dimensions that indicates the design pressure in bar at room temperature (20° C). The permissible pressure is correspondingly smaller at higher temperatures, depending on the permissible material characteristics (yield point).
