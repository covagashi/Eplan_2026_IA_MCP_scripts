# DMDELETEDOBJECTINFO_EDITINGAREA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_EDITINGAREA().html

---

Defined working section # 36617.

Syntax

**C#**



public PropertyValue DMDELETEDOBJECTINFO_EDITINGAREA {get; set;}

public:

property PropertyValue^ DMDELETEDOBJECTINFO_EDITINGAREA {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

The property is used during the revisioning of defined working sections. Displays the name of the defined working section to which the page belongs in the Deleted pages dialog.
