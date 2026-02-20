# FUNC_DEVICETAG_FULL_WITHSEPARATOR Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_FULL_WITHSEPARATOR().html

---

DT (full, without project structures, with preceding sign) # 20213.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_FULL_WITHSEPARATOR {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_FULL_WITHSEPARATOR {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the device tag without the project structures, but with information about the preceding sign.

Example: "-K1" is output for "=A1-K1," "-K1" is output for "-K1" and "-K1-K2" is output for "=A1-K1-K2".
