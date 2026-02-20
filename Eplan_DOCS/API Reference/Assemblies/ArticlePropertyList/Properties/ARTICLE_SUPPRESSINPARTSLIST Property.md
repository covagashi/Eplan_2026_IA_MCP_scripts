# ARTICLE_SUPPRESSINPARTSLIST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUPPRESSINPARTSLIST().html

---

Suppress in bill of materials # 22886.

Syntax

**C#**



public PropertyValue ARTICLE_SUPPRESSINPARTSLIST {get; set;}

public:

property PropertyValue^ ARTICLE_SUPPRESSINPARTSLIST {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, the part is suppressed in the bill of materials. A part identified in this way is neither displayed in the bill of materials navigator nor output in the corresponding part assemblies or via the interfaces for manufacturing data. This part cannot be ordered, but it can be a component of a module or an assembly (for example a plug in a prefabricated cable, where the plug is permanently connected to the cable).
