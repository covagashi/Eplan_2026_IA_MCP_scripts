# PROJ_CREATORNOTE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CREATORNOTE().html

---

Creator: Description # 10247.

Syntax

**C#**



public PropertyValue PROJ_CREATORNOTE {get; set;}

public:

property PropertyValue^ PROJ_CREATORNOTE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is used for entering internal information or remarks, such as "responsible for sales, part......, good credit, etc." and so on. The property can be automatically populated with the relevant manufacturer/supplier data from parts management via project management.
