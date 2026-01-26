# FUNC_SUFFIX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_SUFFIX().html

---

DT: Subcounter # 20015.

Syntax

**C#**



public PropertyValue FUNC_SUFFIX {get; set;}

public:

property PropertyValue^ FUNC_SUFFIX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Suffix for the DT.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
