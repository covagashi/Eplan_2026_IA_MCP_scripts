# ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX().html

---

Current carrying capacity (resistive load, DC), max. # 26156.

Syntax

**C#**



public PropertyValue ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX {get; set;}

public:

property PropertyValue^ ARTICLE_CURRENT_LOAD_RESISTIVE_LOAD_DC_MAX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The maximum electrical current with which a device or item may be loaded so that the device or item is in the specification range if only external ohmic resistors are connected in the closed circuit.
