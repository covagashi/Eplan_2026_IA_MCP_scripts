# ARTICLE_SLOT_GAP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SLOT_GAP().html

---

Slot width # 22286.

Syntax

**C#**



public PropertyValue ARTICLE_SLOT_GAP {get; set;}

public:

property PropertyValue^ ARTICLE_SLOT_GAP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Width of a slot between two wire duct fingers. This part property is required solely for the manufacturing data export for the Rittal Secarex cutting center. This property does not have any influence on the graphical representation of the wire duct in a layout space.
