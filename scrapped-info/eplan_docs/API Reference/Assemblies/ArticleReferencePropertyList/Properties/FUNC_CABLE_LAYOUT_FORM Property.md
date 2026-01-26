# FUNC_CABLE_LAYOUT_FORM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~FUNC_CABLE_LAYOUT_FORM().html

---

Cable assignment diagram form # 20092.

Syntax

**C#**



public PropertyValue FUNC_CABLE_LAYOUT_FORM {get; set;}

public:

property PropertyValue^ FUNC_CABLE_LAYOUT_FORM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Shows the form to be used for the cable assignment diagram. For the report, only those cables are considered which are assigned a form in the property "Cable assignment diagram form". All other cables are ignored.
