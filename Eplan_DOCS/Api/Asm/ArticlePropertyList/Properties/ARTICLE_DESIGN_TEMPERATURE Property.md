# ARTICLE_DESIGN_TEMPERATURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DESIGN_TEMPERATURE().html

---

Design temperature # 26083.

Syntax

**C#**



public PropertyValue ARTICLE_DESIGN_TEMPERATURE {get; set;}

public:

property PropertyValue^ ARTICLE_DESIGN_TEMPERATURE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum or minimum temperature at which a system must work efficiently and reliably. In systems that work with fluids (liquids or gases), this is the temperature of the fluid that is taken as the basis for determining the calculation temperature of each item (EN 764).
