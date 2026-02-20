# FUNC_ARTICLE_REPORT_IDENTIFIER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_REPORT_IDENTIFIER(Int32).html

---

Identifier for reports # 20858.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_REPORT_IDENTIFIER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_REPORT_IDENTIFIER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 50.

The property can be used in filters for conditional forms to specify the subform to be reported in the main form. The value of the part property "Identifier for reports" (ID 22214) is displayed via the index.
