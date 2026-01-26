# PROJ_CUSTOMERNOTE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMERNOTE().html

---

Customer: Description # 10117.

Syntax

**C#**



public PropertyValue PROJ_CUSTOMERNOTE {get; set;}

public:

property PropertyValue^ PROJ_CUSTOMERNOTE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is used for entering internal information or remarks, such as "responsible for sales, part ...., good credit" and so on. The property can be automatically populated with the relevant customer data from parts management via project management.
