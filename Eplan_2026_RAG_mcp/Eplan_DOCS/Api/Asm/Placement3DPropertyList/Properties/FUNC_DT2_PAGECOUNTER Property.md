# FUNC_DT2_PAGECOUNTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_DT2_PAGECOUNTER().html

---

DT (subordinate): Page # 20170.

Syntax

**C#**



public PropertyValue FUNC_DT2_PAGECOUNTER {get; set;}

public:

property PropertyValue^ FUNC_DT2_PAGECOUNTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Name of the page, can be used in the subordinate DT. This property is available only in certain, customer-specific Eplan versions, and can be used if you have selected the "Edit DT in individual fields" project setting.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
