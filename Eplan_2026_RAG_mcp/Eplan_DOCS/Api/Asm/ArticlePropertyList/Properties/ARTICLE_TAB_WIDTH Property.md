# ARTICLE_TAB_WIDTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_TAB_WIDTH().html

---

Finger width # 22285.

Syntax

**C#**



public PropertyValue ARTICLE_TAB_WIDTH {get; set;}

public:

property PropertyValue^ ARTICLE_TAB_WIDTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Width of a wire duct finger. This part property is required solely for the manufacturing data export for the Rittal Secarex cutting center. This property does not have any influence on the graphical representation of the wire duct in a layout space.
