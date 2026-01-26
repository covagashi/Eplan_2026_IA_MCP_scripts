# ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP().html

---

Suitable for degree of protection (IP) # 26358.

Syntax

**C#**



public PropertyValue ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP {get; set;}

public:

property PropertyValue^ ARTICLE_SUITABLE_FOR_PROTECTION_CLASS_IP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Classification of the protection of a device or a component against the penetration of foreign objects and water. The IP degree of protection (International Protection) is specified by two digits. The first digit describes the protection against foreign objects and contact. The second digit describes the protection against water.
