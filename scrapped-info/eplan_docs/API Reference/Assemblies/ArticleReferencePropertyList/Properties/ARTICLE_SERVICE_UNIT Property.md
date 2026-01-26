# ARTICLE_SERVICE_UNIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_SERVICE_UNIT().html

---

Performance unit (bill of quantities) # 26429.

Syntax

**C#**



public PropertyValue ARTICLE_SERVICE_UNIT {get; set;}

public:

property PropertyValue^ ARTICLE_SERVICE_UNIT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Measuring unit in which the output to be provided - in accordance with the performance catalog - is specified, for example cubic meter (m³) for concrete work or piece (unit) for individual items such as windows or doors. The bill of quantities describes all the services, materials and work that are required for a project or a procurement and serves as a basis for offers by suppliers or service providers.
