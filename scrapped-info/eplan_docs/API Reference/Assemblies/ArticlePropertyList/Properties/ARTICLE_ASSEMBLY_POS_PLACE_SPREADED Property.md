# ARTICLE_ASSEMBLY_POS_PLACE_SPREADED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ASSEMBLY_POS_PLACE_SPREADED().html

---

Distributed placement of assembly # 22040.

Syntax

**C#**



public PropertyValue ARTICLE_ASSEMBLY_POS_PLACE_SPREADED {get; set;}

public:

property PropertyValue^ ARTICLE_ASSEMBLY_POS_PLACE_SPREADED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Property of a part variant. Controls how an assembly acts in Eplan Pro Panel: If the property is enabled, the assembly is broken apart in Eplan Pro Panel, so that the single parts can be individually placed (for example main switch distributed between panel and door). If the property is not enabled, the assemblies act as contactors with auxiliary contacts that are placed together and are defined as an assembly in the bill of materials.
