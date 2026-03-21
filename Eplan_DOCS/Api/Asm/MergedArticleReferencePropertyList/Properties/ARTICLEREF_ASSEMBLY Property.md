# ARTICLEREF_ASSEMBLY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLEREF_ASSEMBLY().html

---

Assembly # 20492.

Syntax

**C#**



public PropertyValue ARTICLEREF_ASSEMBLY {get; set;}

public:

property PropertyValue^ ARTICLEREF_ASSEMBLY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

A collection of parts that belong to a device (e.g. a pushbutton with a normally open contact, the appropriate mounting and the button). An assembly has its own part number and can also contain (sub) assemblies.
