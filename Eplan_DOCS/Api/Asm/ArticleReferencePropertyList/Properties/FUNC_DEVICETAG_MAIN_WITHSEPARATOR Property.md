# FUNC_DEVICETAG_MAIN_WITHSEPARATOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_MAIN_WITHSEPARATOR().html

---

DT (superior, without project structures, with preceding sign) # 20211.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_MAIN_WITHSEPARATOR {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_MAIN_WITHSEPARATOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the superior device tag without the project structures, but with information about the preceding sign.

Example: "-U1" is output for "=A+O-U1-K1".
