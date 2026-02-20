# ARTICLE_DISTANCE_WIRE_HOLD_BACK_NOSE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISTANCE_WIRE_HOLD_BACK_NOSE().html

---

Distance of the pinch point # 22287.

Syntax

**C#**



public PropertyValue ARTICLE_DISTANCE_WIRE_HOLD_BACK_NOSE {get; set;}

public:

property PropertyValue^ ARTICLE_DISTANCE_WIRE_HOLD_BACK_NOSE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Distance of the pinch point from a wire duct fin. This part property is required solely for the manufacturing data export for the Rittal Secarex cutting center. This property does not have any influence on the graphical representation of the wire duct in a layout space.
