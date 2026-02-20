# ARTICLE_ACCESSORYID Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ACCESSORYID().html

---

Accessory code # 22025.

Syntax

**C#**



public PropertyValue ARTICLE_ACCESSORYID {get; set;}

public:

property PropertyValue^ ARTICLE_ACCESSORYID {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property should no longer be used and is only available with old Eplan versions for reasons of compatibility. In older Eplan projects (created with Version 1.9 or older), this property was used to assign accessory parts to a part; parts and accessory parts with the same accessory code were grouped together.
