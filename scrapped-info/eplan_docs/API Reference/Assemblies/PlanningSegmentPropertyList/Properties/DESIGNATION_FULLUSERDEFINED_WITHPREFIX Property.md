# DESIGNATION_FULLUSERDEFINED_WITHPREFIX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic776.html

---

Functional assignment (main identifier) # 1300.

Syntax

**C#**



public PropertyValue DESIGNATION_FUNCTIONALASSIGNMENT {get; set;}

public:

property PropertyValue^ DESIGNATION_FUNCTIONALASSIGNMENT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is used as part of a name. In order to set it, member `NameParts` must be used on object which name will be changed. Additionally for setting this property on a Page object, a function Page::SetName() or the Page constructor can be used.
