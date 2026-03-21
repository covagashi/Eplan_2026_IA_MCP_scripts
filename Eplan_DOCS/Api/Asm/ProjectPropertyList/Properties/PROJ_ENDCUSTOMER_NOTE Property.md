# PROJ_ENDCUSTOMER_NOTE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_ENDCUSTOMER_NOTE().html

---

End customer: Description # 10147.

Syntax

**C#**



public PropertyValue PROJ_ENDCUSTOMER_NOTE {get; set;}

public:

property PropertyValue^ PROJ_ENDCUSTOMER_NOTE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is used for entering internal information or remarks, such as "responsible for sales, part ...., good credit" and so on. The property can be automatically populated with the relevant customer data from parts management via project management.
