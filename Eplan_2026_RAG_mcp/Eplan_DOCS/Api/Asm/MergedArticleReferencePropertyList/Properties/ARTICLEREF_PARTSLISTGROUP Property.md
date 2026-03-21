# ARTICLEREF_PARTSLISTGROUP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_PARTSLISTGROUP().html

---

Bill of materials group # 22289.

Syntax

**C#**



public PropertyValue ARTICLEREF_PARTSLISTGROUP {get; set;}

public:

property PropertyValue^ ARTICLEREF_PARTSLISTGROUP {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

You can use this property to group the parts data of components, serial machines, etc. and to make these groups visible in the bill of materials navigator. The property can be used for filtering in the bill of materials and 3D mounting layout navigator and is available in the reports for the bill of materials and for editing in tables.
