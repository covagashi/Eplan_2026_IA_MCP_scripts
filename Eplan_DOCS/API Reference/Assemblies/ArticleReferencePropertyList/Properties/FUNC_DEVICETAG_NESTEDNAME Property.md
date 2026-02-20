# FUNC_DEVICETAG_NESTEDNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_DEVICETAG_NESTEDNAME().html

---

Subordinate product aspect incl. name supplement # 20336.

Syntax

**C#**



public PropertyValue FUNC_DEVICETAG_NESTEDNAME {get; set;}

public:

property PropertyValue^ FUNC_DEVICETAG_NESTEDNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the subordinate part of the full name of a function without the project structures.

Example: "X1" is output for a terminal strip "=A+O-U1-X1" and "X2:3" is output for a terminal "=A-U2-X2:3". This corresponds to the output for the property DT (subordinate, without project structures) (ID 20004) with additional specification of the terminal or connection designation.
