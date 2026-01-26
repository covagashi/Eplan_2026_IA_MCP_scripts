# FUNC_SUPPRESSCROSSREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_SUPPRESSCROSSREFERENCE().html

---

Cross-reference display # 20021.

Syntax

**C#**



public PropertyValue FUNC_SUPPRESSCROSSREFERENCE {get; set;}

public:

property PropertyValue^ FUNC_SUPPRESSCROSSREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies the display of cross-references:

0 = Automatic display (cross-references are only then displayed if the visible DT is not blank).

1 = Never display

2 = Always display.
