# FUNC_DT2_FUNCTIONCODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~FUNC_DT2_FUNCTIONCODE().html

---

DT (subordinate): Application # 20175.

Syntax

**C#**



public PropertyValue FUNC_DT2_FUNCTIONCODE {get; set;}

public:

property PropertyValue^ FUNC_DT2_FUNCTIONCODE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Can be used in the subordinate DT. This property is available only in certain, customer-specific Eplan versions, and can be used if you have selected the "Edit DT in individual fields" project setting.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
