# FUNC_COMPONENTNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_COMPONENTNUMBER().html

---

Item number # 20318.

Syntax

**C#**



public PropertyValue FUNC_COMPONENTNUMBER {get; set;}

public:

property PropertyValue^ FUNC_COMPONENTNUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is used to map the designations used in the standard DIN ISO 1219-2 for fluid power in Eplan. For fluid power devices the subcounter of the device is displayed here, meaning the contents of the property DT: Subcounter (ID 20015).

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
