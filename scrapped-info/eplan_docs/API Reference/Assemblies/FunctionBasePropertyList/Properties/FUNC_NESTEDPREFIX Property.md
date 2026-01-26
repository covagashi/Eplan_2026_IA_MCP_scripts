# FUNC_NESTEDPREFIX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBasePropertyList~FUNC_NESTEDPREFIX().html

---

DT (subordinate): Prefix # 20016.

Syntax

**C#**



public PropertyValue FUNC_NESTEDPREFIX {get; set;}

public:

property PropertyValue^ FUNC_NESTEDPREFIX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Shows the prefix before an identifier in the subordinate DT. Any prefix can be chosen, but a number is most practical. For example, you receive a DT "4K5" with the digit "4" as the prefix. You also obtain this type of DT when you display the page number in the DT; in this case the DT changes when you change the page number. If you use a fixed prefix instead, then the DT does not change.

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
