# ARTICLE_CABLEDESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_CABLEDESIGNATION().html

---

Cable / Conduit: Designation in graphic # 22064.

Syntax

**C#**



public PropertyValue ARTICLE_CABLEDESIGNATION {get; set;}

public:

property PropertyValue^ ARTICLE_CABLEDESIGNATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property of a part variant. This field is provided for the entry of text to be later displayed next to the cable in the schematic, e.g., "OELFLEX-SERVO-FD 4G1.5+2x(2x0.75StD) CP".
