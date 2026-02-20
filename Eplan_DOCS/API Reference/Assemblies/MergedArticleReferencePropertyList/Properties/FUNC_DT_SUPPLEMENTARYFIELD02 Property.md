# FUNC_DT_SUPPLEMENTARYFIELD02 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~FUNC_DT_SUPPLEMENTARYFIELD02().html

---

DT: Supplementary field 2 # 20157.

Syntax

**C#**



public PropertyValue FUNC_DT_SUPPLEMENTARYFIELD02 {get; set;}

public:

property PropertyValue^ FUNC_DT_SUPPLEMENTARYFIELD02 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Can be used in the DT. This property is available only in certain, customer-specific Eplan versions, and can be used if you have selected the "Edit DT in individual fields" project setting.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
