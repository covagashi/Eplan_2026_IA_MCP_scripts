# FUNC_DEVICETAG_MAINNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_MAINNAME().html

---

Superior product aspect incl. name supplement # 20335.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_MAINNAME {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_MAINNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the superior part of the full name of a function without project structures.

Example: "U1" is output for a terminal strip "=A+O-U1-X1" and "X2:3" is output for a terminal "=A-X2:3". If the function has a subordinate DT, no name supplement is output. "U1" is then output at a terminal "=A+O-U1-X1:1". This corresponds to the output for the property DT (superior, without project structures) (ID 20003) with additional specification of the terminal or connection designation.
