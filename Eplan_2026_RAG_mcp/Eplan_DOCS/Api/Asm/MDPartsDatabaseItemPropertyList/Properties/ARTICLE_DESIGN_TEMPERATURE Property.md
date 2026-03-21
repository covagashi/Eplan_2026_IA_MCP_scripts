# ARTICLE_DESIGN_TEMPERATURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_DESIGN_TEMPERATURE().html

---

Design temperature # 26083.

Syntax

**C#**



public MDPropertyValue ARTICLE_DESIGN_TEMPERATURE {get; set;}

public:

property MDPropertyValue^ ARTICLE_DESIGN_TEMPERATURE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Maximum or minimum temperature at which a system must work efficiently and reliably. In systems that work with fluids (liquids or gases), this is the temperature of the fluid that is taken as the basis for determining the calculation temperature of each item (EN 764).
