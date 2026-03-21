# ARTICLE_MIDDLEOFFSET Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_MIDDLEOFFSET().html

---

Center mismatch # 22215.

Syntax

**C#**



public PropertyValue ARTICLE_MIDDLEOFFSET {get; set;}

public:

property PropertyValue^ ARTICLE_MIDDLEOFFSET {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

If you do not want the part to be centered in the front view, enter the offset relative to the middle of the mounting rail. The item will then be automatically offset by this value.
