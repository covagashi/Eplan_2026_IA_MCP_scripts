# PAGE_PAGENAMES_WITH_PROPERTY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_PAGENAMES_WITH_PROPERTY().html

---

Page names per property # 11063.

Syntax

**C#**



public PropertyValue PAGE_PAGENAMES_WITH_PROPERTY {get; set;}

public:

property PropertyValue^ PAGE_PAGENAMES_WITH_PROPERTY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Shows the names of the pages with a specified property. The property is specified in the "Number of pages / Page name per property" project setting. A report run is used to list the pages with the same value as this property, and the page names are written to the "Page names per property" property.
