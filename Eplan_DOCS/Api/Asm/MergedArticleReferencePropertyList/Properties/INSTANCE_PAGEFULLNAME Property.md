# INSTANCE_PAGEFULLNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~INSTANCE_PAGEFULLNAME().html

---

Page name (full) # 19023.

Syntax

**C#**



public PropertyValue INSTANCE_PAGEFULLNAME {get; set;}

public:

property PropertyValue^ INSTANCE_PAGEFULLNAME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

For component or part placements, outputs the full page names (page name + all identifier blocks) of the page on which the corresponding component or item is placed.
