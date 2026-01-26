# ARTICLE_DOES_NOT_NEED_DRILL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DOES_NOT_NEED_DRILL().html

---

Part does not require a drilling pattern # 22394.

Syntax

**C#**



public PropertyValue ARTICLE_DOES_NOT_NEED_DRILL {get; set;}

public:

property PropertyValue^ ARTICLE_DOES_NOT_NEED_DRILL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Specifies that no drill holes are required in the mounting panel for the part. This means that the part can be used without additional drill holes or special mounting preparations.
